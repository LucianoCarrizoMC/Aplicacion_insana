class Usuario:
    """
    Clase para representar un usuario en el sistema.

    Attributes:
        id_usuario (int): ID único del usuario.
        nombre_usuario (str): Nombre de usuario.
        contrasenia (str): Contraseña del usuario.
        rol_id (int): ID del rol asociado al usuario.
    """

    def __init__(self, id_usuario, nombre_usuario, contrasenia, rol_id):
        """
        Inicializa un objeto de tipo Usuario.

        Args:
            id_usuario (int): ID único del usuario.
            nombre_usuario (str): Nombre de usuario.
            contrasenia (str): Contraseña del usuario.
            rol_id (int): ID del rol asociado al usuario.
        """
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia
        self.rol_id = rol_id

    def get_id_usuario(self):
        """
        Obtiene el ID del usuario.

        Returns:
            int: ID del usuario.
        """
        return self.id_usuario

    def get_nombre_usuario(self):
        """
        Obtiene el nombre de usuario.

        Returns:
            str: Nombre de usuario.
        """
        return self.nombre_usuario

    def get_contrasenia(self):
        """
        Obtiene la contraseña del usuario.

        Returns:
            str: Contraseña del usuario.
        """
        return self.contrasenia

    def get_rol_id(self):
        """
        Obtiene el ID del rol asociado al usuario.

        Returns:
            int: ID del rol.
        """
        return self.rol_id
