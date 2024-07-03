class Tipo:
    """
    Clase para representar un tipo de tique en el sistema.

    Attributes:
        id_tipo (int): ID único del tipo de tique.
        nombre_tipo (str): Nombre del tipo de tique.
    """

    def __init__(self, id_tipo, nombre_tipo):
        """
        Inicializa un objeto de tipo Tipo.

        Args:
            id_tipo (int): ID único del tipo de tique.
            nombre_tipo (str): Nombre del tipo de tique.
        """
        self.id_tipo = id_tipo
        self.nombre_tipo = nombre_tipo

    def get_id_tipo(self):
        """
        Obtiene el ID del tipo de tique.

        Returns:
            int: ID del tipo de tique.
        """
        return self.id_tipo

    def get_nombre_tipo(self):
        """
        Obtiene el nombre del tipo de tique.

        Returns:
            str: Nombre del tipo de tique.
        """
        return self.nombre_tipo

    def set_nombre_tipo(self, nombre_tipo):
        """
        Actualiza el nombre del tipo de tique.

        Args:
            nombre_tipo (str): Nuevo nombre del tipo de tique.
        """
        self.nombre_tipo = nombre_tipo
