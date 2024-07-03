class Estado:
    """
    Representa un estado dentro del sistema.

    Attributes:
        id_estado (int): Identificador único del estado.
        nombre_estado (str): Nombre descriptivo del estado.

    Methods:
        get_id_estado():
            Devuelve el ID del estado.
        
        get_nombre_estado():
            Devuelve el nombre del estado.
        
        set_nombre_estado(nombre_estado):
            Establece un nuevo nombre para el estado.
    """

    def __init__(self, id_estado, nombre_estado):
        """
        Inicializa una nueva instancia de Estado.

        Args:
            id_estado (int): ID del estado.
            nombre_estado (str): Nombre del estado.
        """
        self.id_estado = id_estado
        self.nombre_estado = nombre_estado

    def get_id_estado(self):
        """
        Obtiene el ID del estado.

        Returns:
            int: ID del estado.
        """
        return self.id_estado

    def get_nombre_estado(self):
        """
        Obtiene el nombre del estado.

        Returns:
            str: Nombre del estado.
        """
        return self.nombre_estado

    def set_nombre_estado(self, nombre_estado):
        """
        Establece un nuevo nombre para el estado.

        Args:
            nombre_estado (str): Nuevo nombre del estado.
        """
        self.nombre_estado = nombre_estado
