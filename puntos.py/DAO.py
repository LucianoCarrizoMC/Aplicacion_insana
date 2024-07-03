# pip install mysql-connector-python
import mysql.connector
import credenciales
from Tique import Tique
from Cliente import Cliente
from Usuario import Usuario
from Area import Area
from Criticidad import Criticidad
from Tipo import Tipo

class DAO:
    """Clase para gestionar las operaciones de acceso a datos (DAO) con una base de datos MySQL.
    """
    def __init__(self):
        """
        Inicializa una instancia de la clase DAO.
        """
        pass
    
    def conectar(self):
        """
        Establece la conexión con la base de datos utilizando las credenciales proporcionadas.
        """
        self.__conexion = mysql.connector.connect(**credenciales.get_credenciales())
        self.__cursor = self.__conexion.cursor()

    def cerrar(self):
        """
        Cierra la conexión con la base de datos y realiza un commit de las transacciones.
        """
        self.__conexion.commit()
        self.__conexion.close()

    def buscarAreaPorNombre(self, nombreArea):
        """
        Busca un área por su nombre en la base de datos.

        Args:
            nombreArea (str): Nombre del área a buscar.

        Returns:
            None
        """
        self.conectar()
        sql_select_area = "SELECT ID_Area FROM area WHERE Nombre_Area = %s"
        values_select_cliente = (nombreArea,)
        self.__cursor.execute(sql_select_area, values_select_cliente)
        print(self.__cursor.execute(sql_select_area, values_select_cliente))
        self.cerrar()

    def registrarTique(self, tique: Tique, cliente: Cliente):
        """
        Registra un nuevo tique en la base de datos, incluyendo el cliente si no existe.

        Args:
            tique (Tique): Objeto Tique a registrar.
            cliente (Cliente): Objeto Cliente asociado al tique.

        Returns:
            None
        """
        self.conectar()
        
        # Primero, verificamos si el cliente ya existe en la base de datos
        sql_select_cliente = "SELECT id_cliente FROM cliente WHERE rut = %s"
        values_select_cliente = (cliente.get_rut(),)

        self.__cursor.execute(sql_select_cliente, values_select_cliente)
        resultado_cliente = self.__cursor.fetchone()

        # Si el cliente no existe en la base de datos, lo insertamos
        if not resultado_cliente:
            sql_insert_cliente = "INSERT INTO cliente (Nombre_Cliente, Rut, Telefono, Correo_Electronico) VALUES (%s, %s, %s, %s)"
            values_insert_cliente = (
                cliente.get_nombre_cliente(),
                cliente.get_rut(),
                cliente.get_telefono(),
                cliente.get_correo_electronico(),
            )
            self.__cursor.execute(sql_insert_cliente, values_insert_cliente)
            cliente_id = self.__cursor.lastrowid
        else:
            cliente_id = resultado_cliente[0]

        # Ahora podemos insertar el tique utilizando el ID del cliente
        sql_insert_tique = "INSERT INTO tique (Detalle_servicio, Fecha_Creacion, Detalle_Problema, area_ID_Area1, tipo_ID_Tipo1, cliente_ID_cliente, criticidad_ID_Criticidad, estado_ID_Estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values_insert_tique = (
            tique.get_detalle_servicio(),
            tique.get_fecha_creacion(),  # Fecha de creación como objeto date
            tique.get_detalle_problema(),
            tique.get_area_id(),
            tique.get_tipo_id(),
            cliente_id,
            tique.get_criticidad_id(),
            tique.get_estado_id(),
        )
        print(values_insert_tique)
        self.__cursor.execute(sql_insert_tique, values_insert_tique)

        self.cerrar()


    def obtenerTiques(self):
        """
        Obtiene todos los tiques de la base de datos.

        Returns:
            list: Lista de objetos Tique.
        """
        self.conectar()
        sql = "SELECT * FROM tique"
        self.__cursor.execute(sql)
        resultados = self.__cursor.fetchall()
        tiques = []

        for registro in resultados:
            tique = Tique(
                id_tique=registro[0],
                detalle_servicio=registro[1],
                fecha_creacion=registro[2],
                detalle_problema=registro[3],
                area_id=registro[4],
                tipo_id=registro[5],
                criticidad_id=registro[6],
                cliente_id=registro[7],
                estado_id=registro[8],
            )
            tiques.append(tique)

        self.cerrar()
        return tiques


    def obtenerTique(self, id_tique: int):
        """
        Obtiene un tique específico de la base de datos por su ID.

        Args:
            id_tique (int): ID del tique a obtener.

        Returns:
            Tique: Objeto Tique con los datos del tique especificado.
        """
        self.conectar()
        sql = "SELECT * FROM tique WHERE id_tique = %s"
        values = (id_tique,)
        self.__cursor.execute(sql, values)
        registro = self.__cursor.fetchone()
        self.cerrar()
        if registro:
            tique = Tique(
                id_tique=registro[0],
                nombre_cliente=registro[1],
                rut_cliente=registro[2],
                telefono_cliente=registro[3],
                correo_cliente=registro[4],
                tipo_tique=registro[5],
                criticidad=registro[6],
                detalle_servicio=registro[7],
                detalle_problema=registro[8],
                area_id=registro[9],
                tipo_id=registro[10],
                cliente_id=registro[11],
                estado_id=registro[12]
            )
            return tique
        return None

    def actualizarTique(self, tique: Tique):
        """
        Actualiza un tique existente en la base de datos.

        Args:
            tique (Tique): Objeto Tique con los datos actualizados.

        Returns:
            None
        """
        self.conectar()
        sql = "UPDATE tique SET nombre_cliente=%s, rut_cliente=%s, telefono_cliente=%s, correo_cliente=%s, tipo_tique=%s, criticidad=%s, detalle_servicio=%s, detalle_problema=%s, area_id=%s, tipo_id=%s, cliente_id=%s, estado_id=%s WHERE id_tique=%s"
        values = (
            tique.nombre_cliente,
            tique.rut_cliente,
            tique.telefono_cliente,
            tique.correo_cliente,
            tique.tipo_tique,
            tique.criticidad,
            tique.detalle_servicio,
            tique.detalle_problema,
            tique.area_id,
            tique.tipo_id,
            tique.cliente_id,
            tique.estado_id,
            tique.id_tique
        )
        self.__cursor.execute(sql, values)
        self.cerrar()
    def registrar_usuario(self, usuario: Usuario):
        """
        Registra un nuevo usuario en la base de datos.

        Args:
            usuario (Usuario): Objeto Usuario a registrar.

        Returns:
            None
        """
        self.conectar()

        # Consultar si el rol_id existe en la tabla de roles
        sql_select_rol = "SELECT ID_Rol FROM rol WHERE ID_Rol = %s"
        values_select_rol = (usuario.get_rol_id(),)
        self.__cursor.execute(sql_select_rol, values_select_rol)
        resultado_rol = self.__cursor.fetchone()

        if not resultado_rol:
            # Si el rol_id no existe en la tabla de roles, mostrar un mensaje de error y detener el registro.
            self.cerrar()
            return

        # Resto del código para registrar el usuario en la tabla de usuarios
        sql_insert_usuario = "INSERT INTO usuario (Nombre_Usuario, Contrasenia, rol_ID_Rol) VALUES (%s, %s, %s)"
        values_insert_usuario = (usuario.get_nombre_usuario(), usuario.get_contrasenia(), usuario.get_rol_id())
        self.__cursor.execute(sql_insert_usuario, values_insert_usuario)

        self.cerrar()



    def verificar_credenciales(self, nombre: str, contraseña: str) -> bool:
        """
        Verifica las credenciales de un usuario en la base de datos.

        Args:
            nombre (str): Nombre de usuario.
            contraseña (str): Contraseña del usuario.

        Returns:
            bool: True si las credenciales son correctas, False en caso contrario.
        """
        self.conectar()
        sql = "SELECT * FROM usuario WHERE Nombre_Usuario = %s AND Contrasenia = %s"
        values = (nombre, contraseña)
        self.__cursor.execute(sql, values)
        resultado = self.__cursor.fetchone()
        self.cerrar()
        return resultado is not None
    
    def obtenerNombreArea(self, id_area: int) -> str:
        """
        Obtiene el nombre de un área a partir de su ID.

        Args:
            id_area (int): ID del área.

        Returns:
            str: Nombre del área.
        """
        self.conectar()
        sql = "SELECT Nombre_Area FROM area WHERE ID_Area = %s"
        values = (id_area,)
        self.__cursor.execute(sql, values)
        nombre_area = self.__cursor.fetchone()
        self.cerrar()
        return nombre_area[0] if nombre_area else "Desconocida"
    
    def obtenerNombreTipo(self, id_tipo: int) -> str:
        """
        Obtiene el nombre de un tipo a partir de su ID.

        Args:
            id_tipo (int): ID del tipo.

        Returns:
            str: Nombre del tipo.
        """
        self.conectar()
        sql = "SELECT Nombre_Tipo FROM tipo WHERE ID_Tipo = %s"
        values = (id_tipo,)
        self.__cursor.execute(sql, values)
        nombre_tipo = self.__cursor.fetchone()
        self.cerrar()
        return nombre_tipo[0] if nombre_tipo else "Desconocido"
    
    def obtenerRUTCliente(self, cliente_id):
        """
        Obtiene el nombre de una criticidad a partir de su ID.

        Args:
            id_criticidad (int): ID de la criticidad.

        Returns:
            str: Nombre de la criticidad.
        """
        self.conectar()
        # Realizar la consulta para obtener el RUT del cliente a partir de su ID
        sql = "SELECT rut FROM Cliente WHERE id_cliente = %s"
        values = (cliente_id,)
        self.__cursor.execute(sql,values)
        resultado = self.__cursor.fetchone()
        self.cerrar()
        # Si se encontró el cliente, se devuelve su RUT, de lo contrario, se devuelve None
        if resultado:
            return resultado[0]
        else:
            return None

    def obtenerNombreCriticidad(self, id_criticidad: int) -> str:
        """
        Obtiene el nombre de una criticidad a partir de su ID.

        Args:
        id_criticidad (int): ID de la criticidad.

        Returns:
        str: Nombre de la criticidad si se encuentra, de lo contrario, "Desconocida".
        """
        self.conectar()
        sql = "SELECT Nombre_Criticidad FROM criticidad WHERE ID_Criticidad = %s"
        values = (id_criticidad,)
        self.__cursor.execute(sql, values)
        nombre_criticidad = self.__cursor.fetchone()
        self.cerrar()
        return nombre_criticidad[0] if nombre_criticidad else "Desconocida"
    
    def obtenerCriticidades(self):
        """
        Obtiene todas las criticidades de la base de datos.

        Returns:
        list: Lista de objetos Criticidad.
        """
        self.conectar()

        query = "SELECT ID_Criticidad, Nombre_Criticidad FROM criticidad"
        self.__cursor.execute(query)
        criticidades = [Criticidad(id_criticidad=row[0], nombre_criticidad=row[1]) for row in self.__cursor.fetchall()]

        self.cerrar()

        return criticidades
    
    def obtenerAreas(self):
        """
    Obtiene todas las áreas de la base de datos.

    Returns:
        list: Lista de objetos Area.
    """
        self.conectar()

        query = "SELECT ID_Area, Nombre_Area FROM area"
        self.__cursor.execute(query)
        areas = [Area(id_area=row[0], nombre_area=row[1]) for row in self.__cursor.fetchall()]

        self.cerrar()

        return areas
    
    def obtenerTipos(self):
        """
    Obtiene todos los tipos de la base de datos.

    Returns:
        list: Lista de objetos Tipo.
    """
        self.conectar()

        query = "SELECT ID_Tipo, Nombre_Tipo FROM tipo"
        self.__cursor.execute(query)
        tipos = [Tipo(id_tipo=row[0], nombre_tipo=row[1]) for row in self.__cursor.fetchall()]

        self.cerrar()

        return tipos
    
    def obtenerTiquesPorRutCliente(self, rut):
        """
    Obtiene todos los tiques asociados a un cliente con el RUT especificado.

    Args:
        rut (str): RUT del cliente.

    Returns:
        list: Lista de objetos Tique.
    """
        self.conectar()
        # Implementa la consulta SQL para obtener los tiques del cliente con el RUT especificado
        sql = "SELECT t.* FROM tique t INNER JOIN cliente c ON t.cliente_id = c.id_cliente WHERE c.rut = %s"
        values = (rut,)
        self.__cursor.execute(sql, values)
        results = self.__cursor.fetchall()
        lista_tiques = []
        for row in results:
            tique = Tique(
                id_tique=row[0],
                detalle_servicio=row[1],
                fecha_creacion=row[2],
                detalle_problema=row[3],
                area_id=row[4],
                tipo_id=row[5],
                criticidad_id=row[6],
                cliente_id=row[7],
                estado_id=row[8],
            )
            lista_tiques.append(tique)
        self.cerrar()
        return lista_tiques

    def eliminarTique(self, id_tique):
        """
    Elimina un tique de la base de datos por su ID.

    Args:
        id_tique (int): ID del tique a eliminar.

    Returns:
        None
    """
        self.conectar()
        try:
            # Crear la consulta para eliminar el tique con el ID proporcionado
            query = "DELETE FROM tique WHERE id_tique = %s"
            self.__cursor.execute(query, (id_tique,))
            self.__conexion.commit()
            print("Tique eliminado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al eliminar el tique: {err}")
            # Si ocurre un error, es mejor hacer rollback para deshacer cambios no deseados
            self.__conexion.rollback()
        else:
            print("Operación exitosa.")
        finally:
            # Cerrar el cursor y la conexión
            self.__cursor.close()
            self.__conexion.close()
        self.cerrar()