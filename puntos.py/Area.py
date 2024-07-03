class Area:
    """
    Representa un área de servicio en el sistema.

    Attributes:
        id_area (int): Identificador único del área.
        nombre_area (str): Nombre del área.

    Methods:
        __init__(self, id_area, nombre_area):
            Inicializa una nueva instancia de Area con el ID y nombre especificados.
        
        get_id_area(self):
            Retorna el identificador del área.
        
        get_nombre_area(self):
            Retorna el nombre del área.
        
        set_nombre_area(self, nombre_area):
            Establece el nombre del área.
    """

    def __init__(self, id_area, nombre_area):
        """
        Inicializa una nueva instancia de Area con el ID y nombre especificados.

        Args:
            id_area (int): Identificador único del área.
            nombre_area (str): Nombre del área.
        """
        self.id_area = id_area
        self.nombre_area = nombre_area

    def get_id_area(self):
        """
        Retorna el identificador del área.

        Returns:
            int: Identificador del área.
        """
        return self.id_area

    def get_nombre_area(self):
        """
        Retorna el nombre del área.

        Returns:
            str: Nombre del área.
        """
        return self.nombre_area

    def set_nombre_area(self, nombre_area):
        """
        Establece el nombre del área.

        Args:
            nombre_area (str): Nuevo nombre del área.
        """
        self.nombre_area = nombre_area