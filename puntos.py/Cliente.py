class Cliente:
    """
    Representa un cliente en el sistema.

    Attributes:
        id_cliente (int): Identificador único del cliente.
        nombre_cliente (str): Nombre del cliente.
        rut (str): RUT del cliente.
        correo_electronico (str): Correo electrónico del cliente.
        telefono (str): Número de teléfono del cliente.
        usuario_id (int): Identificador del usuario asociado al cliente.

    Methods:
        __init__(self, id_cliente, nombre_cliente, rut, correo_electronico, telefono, usuario_id):
            Inicializa una nueva instancia de Cliente con los atributos especificados.
        
        get_id_cliente(self):
            Retorna el identificador del cliente.
        
        get_nombre_cliente(self):
            Retorna el nombre del cliente.
        
        get_rut(self):
            Retorna el RUT del cliente.
        
        get_correo_electronico(self):
            Retorna el correo electrónico del cliente.
        
        get_telefono(self):
            Retorna el número de teléfono del cliente.
        
        get_usuario_id(self):
            Retorna el identificador del usuario asociado al cliente.
        
        set_nombre_cliente(self, nombre_cliente):
            Establece el nombre del cliente.
        
        set_rut(self, rut):
            Establece el RUT del cliente.
        
        set_correo_electronico(self, correo_electronico):
            Establece el correo electrónico del cliente.
        
        set_telefono(self, telefono):
            Establece el número de teléfono del cliente.
        
        set_usuario_id(self, usuario_id):
            Establece el identificador del usuario asociado al cliente.
    """

    def __init__(self, id_cliente, nombre_cliente, rut, correo_electronico, telefono, usuario_id):
        """
        Inicializa una nueva instancia de Cliente con los atributos especificados.

        Args:
            id_cliente (int): Identificador único del cliente.
            nombre_cliente (str): Nombre del cliente.
            rut (str): RUT del cliente.
            correo_electronico (str): Correo electrónico del cliente.
            telefono (str): Número de teléfono del cliente.
            usuario_id (int): Identificador del usuario asociado al cliente.
        """
        self.id_cliente = id_cliente
        self.nombre_cliente = nombre_cliente
        self.rut = rut
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.usuario_id = usuario_id

    def get_id_cliente(self):
        """
        Retorna el identificador del cliente.

        Returns:
            int: Identificador del cliente.
        """
        return self.id_cliente

    def get_nombre_cliente(self):
        """
        Retorna el nombre del cliente.

        Returns:
            str: Nombre del cliente.
        """
        return self.nombre_cliente

    def get_rut(self):
        """
        Retorna el RUT del cliente.

        Returns:
            str: RUT del cliente.
        """
        return self.rut

    def get_correo_electronico(self):
        """
        Retorna el correo electrónico del cliente.

        Returns:
            str: Correo electrónico del cliente.
        """
        return self.correo_electronico

    def get_telefono(self):
        """
        Retorna el número de teléfono del cliente.

        Returns:
            str: Número de teléfono del cliente.
        """
        return self.telefono

    def get_usuario_id(self):
        """
        Retorna el identificador del usuario asociado al cliente.

        Returns:
            int: Identificador del usuario asociado al cliente.
        """
        return self.usuario_id

    def set_nombre_cliente(self, nombre_cliente):
        """
        Establece el nombre del cliente.

        Args:
            nombre_cliente (str): Nuevo nombre del cliente.
        """
        self.nombre_cliente = nombre_cliente

    def set_rut(self, rut):
        """
        Establece el RUT del cliente.

        Args:
            rut (str): Nuevo RUT del cliente.
        """
        self.rut = rut

    def set_correo_electronico(self, correo_electronico):
        """
        Establece el correo electrónico del cliente.

        Args:
            correo_electronico (str): Nuevo correo electrónico del cliente.
        """
        self.correo_electronico = correo_electronico

    def set_telefono(self, telefono):
        """
        Establece el número de teléfono del cliente.

        Args:
            telefono (str): Nuevo número de teléfono del cliente.
        """
        self.telefono = telefono

    def set_usuario_id(self, usuario_id):
        """
        Establece el identificador del usuario asociado al cliente.

        Args:
            usuario_id (int): Nuevo identificador del usuario asociado al cliente.
        """
        self.usuario_id = usuario_id
