import pydoc
import os

def generar_documentacion_html():
    """
    Genera documentación HTML para todos los archivos .py en el directorio actual utilizando pydoc.

    Este script busca todos los archivos .py en el directorio actual y genera archivos HTML de documentación
    para cada uno utilizando pydoc.writedoc().

    Requiere que pydoc y os estén disponibles y configurados correctamente en el entorno de ejecución.

    Ejemplo:
        Si ejecutas este script desde el directorio donde están tus archivos .py, generará archivos HTML de
        documentación para cada módulo.

    Nota:
        Asegúrate de tener permisos suficientes para escribir archivos en el directorio actual donde se ejecuta
        este script.

    """
    # Obtener la lista de archivos .py en el directorio actual
    archivos_py = [archivo for archivo in os.listdir() if archivo.endswith('.py')]

    # Generar la documentación HTML para cada archivo .py
    for archivo in archivos_py:
        # Obtener el nombre del módulo sin la extensión .py
        nombre_modulo = os.path.splitext(archivo)[0]
        pydoc.writedoc(nombre_modulo)

# Ejecutar la función para generar la documentación al llamar este script directamente
if __name__ == "__main__":
    generar_documentacion_html()
