class Tique:
    """
    Clase para representar un tique en el sistema.

    Attributes:
        id_tique (int): ID único del tique.
        detalle_servicio (str): Detalle del servicio asociado al tique.
        fecha_creacion (str): Fecha de creación del tique.
        detalle_problema (str): Detalle del problema reportado en el tique.
        area_id (int): ID del área asociada al tique.
        tipo_id (int): ID del tipo de tique.
        criticidad_id (int): ID de la criticidad del tique.
        cliente_id (int): ID del cliente asociado al tique.
        estado_id (int): ID del estado actual del tique.
    """

    def __init__(self, id_tique, detalle_servicio, fecha_creacion, detalle_problema, area_id, tipo_id, criticidad_id, cliente_id, estado_id):
        """
        Inicializa un objeto de tipo Tique.

        Args:
            id_tique (int): ID único del tique.
            detalle_servicio (str): Detalle del servicio asociado al tique.
            fecha_creacion (str): Fecha de creación del tique.
            detalle_problema (str): Detalle del problema reportado en el tique.
            area_id (int): ID del área asociada al tique.
            tipo_id (int): ID del tipo de tique.
            criticidad_id (int): ID de la criticidad del tique.
            cliente_id (int): ID del cliente asociado al tique.
            estado_id (int): ID del estado actual del tique.
        """
        self.id_tique = id_tique
        self.detalle_servicio = detalle_servicio
        self.fecha_creacion = fecha_creacion
        self.detalle_problema = detalle_problema
        self.area_id = area_id
        self.tipo_id = tipo_id
        self.criticidad_id = criticidad_id
        self.cliente_id = cliente_id
        self.estado_id = estado_id

    # Métodos getter para obtener los atributos del tique
    def get_id_tique(self):
        """
        Obtiene el ID del tique.

        Returns:
            int: ID del tique.
        """
        return self.id_tique

    def get_detalle_servicio(self):
        """
        Obtiene el detalle del servicio asociado al tique.

        Returns:
            str: Detalle del servicio.
        """
        return self.detalle_servicio

    def get_fecha_creacion(self):
        """
        Obtiene la fecha de creación del tique.

        Returns:
            str: Fecha de creación en formato string.
        """
        return self.fecha_creacion

    def get_detalle_problema(self):
        """
        Obtiene el detalle del problema reportado en el tique.

        Returns:
            str: Detalle del problema.
        """
        return self.detalle_problema

    def get_area_id(self):
        """
        Obtiene el ID del área asociada al tique.

        Returns:
            int: ID del área.
        """
        return self.area_id

    def get_tipo_id(self):
        """
        Obtiene el ID del tipo de tique.

        Returns:
            int: ID del tipo de tique.
        """
        return self.tipo_id

    def get_criticidad_id(self):
        """
        Obtiene el ID de la criticidad del tique.

        Returns:
            int: ID de la criticidad.
        """
        return self.criticidad_id

    def get_cliente_id(self):
        """
        Obtiene el ID del cliente asociado al tique.

        Returns:
            int: ID del cliente.
        """
        return self.cliente_id

    def get_estado_id(self):
        """
        Obtiene el ID del estado actual del tique.

        Returns:
            int: ID del estado.
        """
        return self.estado_id

    # Métodos setter para actualizar los atributos del tique
    def set_detalle_servicio(self, detalle_servicio):
        """
        Actualiza el detalle del servicio asociado al tique.

        Args:
            detalle_servicio (str): Nuevo detalle del servicio.
        """
        self.detalle_servicio = detalle_servicio

    def set_fecha_creacion(self, fecha_creacion):
        """
        Actualiza la fecha de creación del tique.

        Args:
            fecha_creacion (str): Nueva fecha de creación en formato string.
        """
        self.fecha_creacion = fecha_creacion

    def set_detalle_problema(self, detalle_problema):
        """
        Actualiza el detalle del problema reportado en el tique.

        Args:
            detalle_problema (str): Nuevo detalle del problema.
        """
        self.detalle_problema = detalle_problema

    def set_area_id(self, area_id):
        """
        Actualiza el ID del área asociada al tique.

        Args:
            area_id (int): Nuevo ID del área.
        """
        self.area_id = area_id

    def set_tipo_id(self, tipo_id):
        """
        Actualiza el ID del tipo de tique.

        Args:
            tipo_id (int): Nuevo ID del tipo de tique.
        """
        self.tipo_id = tipo_id

    def set_criticidad_id(self, criticidad_id):
        """
        Actualiza el ID de la criticidad del tique.

        Args:
            criticidad_id (int): Nuevo ID de la criticidad.
        """
        self.criticidad_id = criticidad_id

    def set_cliente_id(self, cliente_id):
        """
        Actualiza el ID del cliente asociado al tique.

        Args:
            cliente_id (int): Nuevo ID del cliente.
        """
        self.cliente_id = cliente_id

    def set_estado_id(self, estado_id):
        """
        Actualiza el ID del estado actual del tique.

        Args:
            estado_id (int): Nuevo ID del estado.
        """
        self.estado_id = estado_id
