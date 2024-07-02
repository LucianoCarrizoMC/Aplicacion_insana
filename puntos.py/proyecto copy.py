import tkinter as tk
from tkinter import ttk
from DAO import DAO
from Tique import Tique
from Cliente import Cliente
from datetime import date
from tkinter import messagebox

class RegistrarTiqueApp:
    """Aplicación para registrar tiques.

    Esta aplicación permite registrar tiques de servicio, consultar y eliminar tiques existentes.
    """
    def __init__(self, root):
        """Inicializa la aplicación de registro de tiques.

        Args:
            root (tk.Tk): La ventana raíz de la aplicación.
        """        
        self.root = root
        self.root.title("Registrar Tique")

        # Obtener el ancho y alto de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Establecer el tamaño de la ventana de la aplicación como un porcentaje de la resolución de pantalla
        app_width = int(screen_width * 0.8)
        app_height = int(screen_height * 0.8)
        self.root.geometry(f"{app_width}x{app_height}")

        self.dao = DAO()
        self.tiques_encontrados = []  # Variable para almacenar los tiques encontrados por RUT
        print(self.tiques_encontrados)

        # Crear un Frame para contener los campos y botón de registro
        frame = ttk.Frame(root)
        frame.pack(expand=True, fill='both')  # Utilizamos pack para que el Frame se expanda

        # Configurar el peso de las filas y columnas para que se ajusten automáticamente
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(11, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        # Crear variables para almacenar la información del tique y los IDs seleccionados
        self.rut_var = tk.StringVar()
        self.nombre_cliente_var = tk.StringVar()
        self.telefono_var = tk.StringVar()
        self.correo_var = tk.StringVar()
        self.tipo_var = tk.StringVar()
        self.criticidad_var = tk.StringVar()
        self.detalle_servicio_var = tk.StringVar()
        self.detalle_problema_var = tk.StringVar()
        self.area_var = tk.StringVar()
        self.id_area_seleccionada = None
        self.id_criticidad_seleccionada = None
        self.id_tipo_tique_seleccionado = None
        self.rut_cliente_var = tk.StringVar()

        # Crear campos de entrada y menús desplegables
        tk.Label(frame, text="RUT del cliente:").grid(row=0, column=0)
        tk.Entry(frame, textvariable=self.rut_var).grid(row=0, column=1)
        
        tk.Label(frame, text="Nombre del cliente:").grid(row=1, column=0)
        tk.Entry(frame, textvariable=self.nombre_cliente_var).grid(row=1, column=1)

        tk.Label(frame, text="Teléfono:").grid(row=2, column=0)
        tk.Entry(frame, textvariable=self.telefono_var).grid(row=2, column=1)

        tk.Label(frame, text="Correo electrónico:").grid(row=3, column=0)
        tk.Entry(frame, textvariable=self.correo_var).grid(row=3, column=1)

        tk.Label(frame, text="Tipo de tique:").grid(row=4, column=0)
        tipos = ["Selecciona El tipo de Tique",'Felicitación', 'Consulta', 'Reclamo', 'Problema']
        self.tipo_menu = ttk.OptionMenu(frame, self.tipo_var, *tipos)
        self.tipo_menu.grid(row=4, column=1)

        tk.Label(frame, text="Criticidad:").grid(row=5, column=0)
        criticidades = ["Seleciona Criticidad",'Baja', 'Media', 'Alta']
        self.criticidad_menu = ttk.OptionMenu(frame, self.criticidad_var, *criticidades)
        self.criticidad_menu.grid(row=5, column=1)

        tk.Label(frame, text="Detalle del servicio:").grid(row=6, column=0)
        tk.Entry(frame, textvariable=self.detalle_servicio_var).grid(row=6, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

        tk.Label(frame, text="Detalle del problema:").grid(row=7, column=0)
        self.detalle_problema_text = tk.Text(frame, height=8, width=50, wrap=tk.WORD, padx=5, pady=5, 
                                            font=("Helvetica", 10))
        self.detalle_problema_text.grid(row=7, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

        tk.Label(frame, text="Área para derivar:").grid(row=8, column=0)
        areas = ["Selecciona una Area","Area 1", "Area 2", "Area 3"]
        self.area_menu = ttk.OptionMenu(frame, self.area_var, *areas)
        self.area_menu.grid(row=8, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

        # Agregar trace para actualizar los IDs seleccionados
        # self.area_var.trace_add("write", self.actualizar_id_area)
        # self.criticidad_var.trace_add("write", self.actualizar_id_criticidad)
        # self.tipo_var.trace_add("write", self.actualizar_id_tipo_tique)

        # Botón para registrar el tique
        tk.Button(frame, text="Registrar Tique", command=self.registrar_tique).grid(row=9, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        # Botón para obtener la lista de tiques
        tk.Button(frame, text="Obtener Tiques", command=self.obtener_tiques).grid(row=10, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # Crear un treeview para mostrar los tiques
        columns = ("ID Tique", "Detalle Servicio", "Fecha Creación", "Área", "Tipo", "Criticidad", "Rut Cliente")
        self.treeview = ttk.Treeview(frame, columns=columns, show="headings")
        for col in columns:
            self.treeview.heading(col, text=col)
        self.treeview.grid(row=11, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Botón para buscar tiques por RUT
        tk.Button(frame, text="Buscar Tique por Rut", command=self.buscar_tiques_por_rut).grid(row=12, column=2, padx=5, pady=5)

        # Configurar el evento para mostrar el tique seleccionado cuando se haga clic en un elemento del treeview
        self.treeview.bind("<ButtonRelease-1>", self.mostrar_tique_seleccionado)

        # Botón para obtener la lista de tiques
        tk.Button(frame, text="Obtener Tiques", command=self.obtener_tiques).grid(row=10, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # Botón para eliminar tique seleccionado
        tk.Button(frame, text="Eliminar Tique", command=self.eliminar_tique).grid(row=12, column=0, padx=5, pady=5)
        

    def actualizar_id_area(self, *args):
        """Actualizar el ID del área seleccionada
        """        
        selected_area = self.area_var.get()
        # Actualizar el ID del área seleccionada
        if selected_area == "Area 1":
            self.id_area_seleccionada = 1
        elif selected_area == "Area 2":
            self.id_area_seleccionada = 2
        elif selected_area == "Area 3":
            self.id_area_seleccionada = 3
        else:
            self.id_area_seleccionada = None  # Opcional: Manejar el caso de "Selecciona una Area"

        print("ID del área seleccionada:", self.id_area_seleccionada)
        print("ID del tipo de tique seleccionado:", self.id_tipo_tique_seleccionado)

    def actualizar_id_criticidad(self, *args):
        """Actualizar el ID de la criticidad seleccionada
        """        
        selected_criticidad = self.criticidad_var.get()
        # Actualizar el ID de la criticidad seleccionada
        if selected_criticidad == "Baja":
            self.id_criticidad_seleccionada = 1
        elif selected_criticidad == "Media":
            self.id_criticidad_seleccionada = 2
        elif selected_criticidad == "Alta":
            self.id_criticidad_seleccionada = 3
        else:
            self.id_criticidad_seleccionada = None  # Opcional: Manejar el caso de "Seleciona Criticidad"

        print("ID de la criticidad seleccionada:", self.id_criticidad_seleccionada)

        print("ID del tipo de tique seleccionado:", self.id_tipo_tique_seleccionado)

    def actualizar_id_tipo_tique(self, *args):
        """Actualizar el ID del tipo de tique seleccionado
        """        
        selected_tipo_tique = self.tipo_var.get()
        # Actualizar el ID del tipo de tique seleccionado
        if selected_tipo_tique == "Felicitación":
            self.id_tipo_tique_seleccionado = 1
        elif selected_tipo_tique == "Consulta":
            self.id_tipo_tique_seleccionado = 2
        elif selected_tipo_tique == "Reclamo":
            self.id_tipo_tique_seleccionado = 3
        elif selected_tipo_tique == "Problema":
            self.id_tipo_tique_seleccionado = 4
        else:
            self.id_tipo_tique_seleccionado = None  # Opcional: Manejar el caso de "Selecciona El tipo de Tique"

        print("ID del tipo de tique seleccionado:", self.id_tipo_tique_seleccionado)

    def actualizar_id_tipo_tique(self, *args):
        self.actualizar_ids_seleccionados()
        print("ID del tipo de tique seleccionado:", self.id_tipo_tique_seleccionado)

    def actualizar_id_criticidad(self, *args):
        self.actualizar_ids_seleccionados()
        print("ID de la criticidad seleccionada:", self.id_criticidad_seleccionada)

    def actualizar_id_area(self, *args):
        self.actualizar_ids_seleccionados()
        print("ID del área seleccionada:", self.id_area_seleccionada)

    def actualizar_ids_seleccionados(self):
    # Actualizar el ID del tipo de tique seleccionado
        selected_tipo_tique = self.tipo_var.get()
        if selected_tipo_tique == "Felicitación":
            self.id_tipo_tique_seleccionado = 1
        elif selected_tipo_tique == "Consulta":
            self.id_tipo_tique_seleccionado = 2
        elif selected_tipo_tique == "Reclamo":
            self.id_tipo_tique_seleccionado = 3
        elif selected_tipo_tique == "Problema":
            self.id_tipo_tique_seleccionado = 4
        else:
            self.id_tipo_tique_seleccionado = None  # Opcional: Manejar el caso de "Selecciona El tipo de Tique"

    # Actualizar el ID de la criticidad seleccionada
        selected_criticidad = self.criticidad_var.get()
        if selected_criticidad == "Baja":
            self.id_criticidad_seleccionada = 1
        elif selected_criticidad == "Media":
            self.id_criticidad_seleccionada = 2
        elif selected_criticidad == "Alta":
            self.id_criticidad_seleccionada = 3
        else:
            self.id_criticidad_seleccionada = None  # Opcional: Manejar el caso de "Selecciona Criticidad"

    # Actualizar el ID del área seleccionada
        selected_area = self.area_var.get()
        if selected_area == "Area 1":
            self.id_area_seleccionada = 1
        elif selected_area == "Area 2":
            self.id_area_seleccionada = 2
        elif selected_area == "Area 3":
            self.id_area_seleccionada = 3
        else:
            self.id_area_seleccionada = None  # Opcional: Manejar el caso de "Selecciona una Area"

    def registrar_tique(self):
        """Registra un tique en la base de datos.
        """
        # Obtener los valores ingresados por el usuario
        rut = self.rut_var.get()
        nombre_cliente = self.nombre_cliente_var.get()
        telefono = self.telefono_var.get()
        correo = self.correo_var.get()
        tipo = self.tipo_var.get()
        criticidad = self.criticidad_var.get()
        detalle_servicio = self.detalle_servicio_var.get()
        detalle_problema = self.detalle_problema_text.get("1.0", tk.END)  # Obtener el contenido del Text
        area = self.area_var.get()

        # Crear un objeto de tipo Tique con la información ingresada
        tique = Tique(
            id_tique=None,
            detalle_servicio=detalle_servicio,
            fecha_creacion=date.today(),  # Utilizamos la fecha actual directamente
            detalle_problema=detalle_problema,
            area_id=area,
            tipo_id=tipo,
            criticidad_id=criticidad,
            cliente_id=None,
            estado_id=1,
        )

        # Crear un objeto de tipo Cliente con la información ingresada
        cliente = Cliente(
            id_cliente=None,
            nombre_cliente=nombre_cliente,
            rut=rut,
            correo_electronico=correo,
            telefono=telefono,
            usuario_id=None,
        )

        # Llamar a la función del DAO para registrar el tique en la base de datos
        self.dao.registrarTique(tique, cliente)

        # Limpiar los campos después de registrar el tique
        self.rut_var.set("")
        self.nombre_cliente_var.set("")
        self.telefono_var.set("")
        self.correo_var.set("")
        self.tipo_var.set("")
        self.criticidad_var.set("")
        self.detalle_servicio_var.set("")
        self.detalle_problema_text.delete("1.0", tk.END)  # Limpiar el contenido del Text
        self.area_var.set("")

    def obtener_tiques(self):
        """Obtiene la lista de tiques desde la base de datos.
        """
        # Llamar a la función del DAO para obtener los tiques
        lista_tiques = self.dao.obtenerTiques()

        # Limpiar el treeview antes de mostrar los nuevos datos
        self.treeview.delete(*self.treeview.get_children())

        # Mostrar los datos en el treeview
        for tique in lista_tiques:
            nombre_area = self.dao.obtenerNombreArea(tique.area_id)
            nombre_tipo = self.dao.obtenerNombreTipo(tique.tipo_id)
            nombre_criticidad = self.dao.obtenerNombreCriticidad(tique.criticidad_id)
            rut_cliente = self.dao.obtenerRUTCliente(tique.cliente_id)

            # Insertar los datos en el treeview
            self.treeview.insert("", "end", values=(tique.id_tique, tique.detalle_servicio, tique.fecha_creacion, nombre_area, nombre_tipo, nombre_criticidad, rut_cliente))

    def buscar_tiques_por_rut(self):
        """Busca tiques en la base de datos por RUT del cliente.
        """
        # Obtener el RUT ingresado por el usuario
        rut_cliente = self.rut_cliente_var.get()

        # Llamar a la función del DAO para obtener los tiques del cliente con el RUT ingresado
        self.tiques_encontrados = self.dao.obtenerTiquesPorRutCliente(rut_cliente)

        # Limpiar el treeview antes de mostrar los nuevos datos
        self.treeview.delete(*self.treeview.get_children())

        # Mostrar los datos en el treeview
        for tique in self.tiques_encontrados:
            nombre_area = self.dao.obtenerNombreArea(tique.area_id)
            nombre_tipo = self.dao.obtenerNombreTipo(tique.tipo_id)
            nombre_criticidad = self.dao.obtenerNombreCriticidad(tique.criticidad_id)
            rut_cliente = self.dao.obtenerRUTCliente(tique.cliente_id)

            # Insertar los datos en el treeview
            self.treeview.insert("", "end", values=(tique.id_tique, tique.detalle_servicio, tique.fecha_creacion, nombre_area, nombre_tipo, nombre_criticidad, rut_cliente))

    def mostrar_tique_seleccionado(self, event):
        """Muestra los detalles del tique seleccionado en el treeview.

        Args:
            event (tk.Event): El evento de clic en el treeview.
        """
        selected_item = self.treeview.focus()
        if selected_item:
            selected_index = self.treeview.index(selected_item)
            if selected_index is not None and 0 <= selected_index < len(self.tiques_encontrados):
                tique_seleccionado = self.tiques_encontrados[selected_index]
                # Resto del código para rellenar los campos con la información del tique seleccionado
                self.rut_var.set(tique_seleccionado.cliente.rut)
                self.nombre_cliente_var.set(tique_seleccionado.cliente.nombre_cliente)

                # Rellenar los campos con la información del tique seleccionado
                self.rut_var.set(tique_seleccionado.cliente.rut)
                self.nombre_cliente_var.set(tique_seleccionado.cliente.nombre_cliente)
                self.telefono_var.set(tique_seleccionado.cliente.telefono)
                self.correo_var.set(tique_seleccionado.cliente.correo_electronico)
                self.tipo_var.set(self.dao.obtenerNombreTipo(tique_seleccionado.tipo_id))
                self.criticidad_var.set(self.dao.obtenerNombreCriticidad(tique_seleccionado.criticidad_id))
                self.detalle_servicio_var.set(tique_seleccionado.detalle_servicio)
                self.detalle_problema_text.delete("1.0", tk.END)
                self.detalle_problema_text.insert(tk.END, tique_seleccionado.detalle_problema)
                self.area_var.set(self.dao.obtenerNombreArea(tique_seleccionado.area_id))
            else:
            # Si el índice no es válido o el tique no existe en la lista, limpiar los campos
                self.rut_var.set("")
                self.nombre_cliente_var.set("")
                self.telefono_var.set("")
                self.correo_var.set("")
                self.tipo_var.set("")
                self.criticidad_var.set("")
                self.detalle_servicio_var.set("")
                self.detalle_problema_text.delete("1.0", tk.END)
                self.area_var.set("")

    def eliminar_tique(self):
        """Elimina el tique seleccionado.
        """
    #Obtener el índice del tique seleccionado en el treeview
        selected_item = self.treeview.focus()
        info_item = self.treeview.item(selected_item)
        id_tiquet = info_item.get("values")[0]
        print(id_tiquet)
        if selected_item:
            mensaje = messagebox.askyesno(self.root, message="¿Estas seguro que quieres eliminar este tique?")
            if(mensaje == True):
                # Llamar a la función del DAO para eliminar el tique de la base de datos
                self.dao.eliminarTique(id_tiquet)

                # Actualizar la lista de tiques en el treeview
                self.obtener_tiques()

                # Limpiar los campos después de eliminar el tique
                self.rut_var.set("")
                self.nombre_cliente_var.set("")
                self.telefono_var.set("")
                self.correo_var.set("")
                self.tipo_var.set("")
                self.criticidad_var.set("")
                self.detalle_servicio_var.set("")
                self.detalle_problema_text.delete("1.0", tk.END)
                self.area_var.set("")
                messagebox.showinfo(self.root, message = "El tique ha sido eliminado")
            else:
                messagebox.showinfo(self.root, message="Se ha cancelado la acción de eliminar tique")
    
# Crear una instancia de Tkinter y la aplicación Registrar Tique
if __name__ == '__main__':
    root = tk.Tk()
    app = RegistrarTiqueApp(root)
    root.mainloop()
