def get_credenciales():
    """
    Retorna un diccionario con las credenciales de conexión a la base de datos.

    Returns:
        dict: Diccionario con las siguientes credenciales:
            - 'host': Dirección del host de la base de datos (localhost en este caso).
            - 'user': Usuario de la base de datos (root en este caso).
            - 'password': Contraseña de acceso a la base de datos (cadena vacía en este caso).
            - 'database': Nombre de la base de datos a la que se desea conectar (sistema2 en este caso).
    """
    credenciales={
        'host' : 'localhost',
        'user' : 'root',
        'password' : '',
        'database' : 'sistema2',
    }
    return credenciales
