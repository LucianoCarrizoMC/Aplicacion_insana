class Criticidad:
    """
    Representa una entidad de criticidad con su identificador y nombre.

    Attributes:
        id_criticidad (int): Identificador único de la criticidad.
        nombre_criticidad (str): Nombre descriptivo de la criticidad.

    Methods:
        get_id_criticidad(self):
            Retorna el identificador de la criticidad.
        
        get_nombre_criticidad(self):
            Retorna el nombre de la criticidad.
        
        set_nombre_criticidad(self, nombre_criticidad):
            Actualiza el nombre de la criticidad con el valor proporcionado.
    """

    def __init__(self, id_criticidad, nombre_criticidad):
        """
        Inicializa una nueva instancia de la clase Criticidad.

        Args:
            id_criticidad (int): Identificador único de la criticidad.
            nombre_criticidad (str): Nombre descriptivo de la criticidad.
        """
        self.id_criticidad = id_criticidad
        self.nombre_criticidad = nombre_criticidad

    def get_id_criticidad(self):
        """
        Retorna el identificador de la criticidad.

        Returns:
            int: Identificador de la criticidad.
        """
        return self.id_criticidad

    def get_nombre_criticidad(self):
        """
        Retorna el nombre de la criticidad.

        Returns:
            str: Nombre de la criticidad.
        """
        return self.nombre_criticidad

    def set_nombre_criticidad(self, nombre_criticidad):
        """
        Actualiza el nombre de la criticidad con el valor proporcionado.

        Args:
            nombre_criticidad (str): Nuevo nombre de la criticidad.
        """
        self.nombre_criticidad = nombre_criticidad
