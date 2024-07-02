import tkinter as tk
from tkinter import ttk, messagebox
from DAO import DAO
from Usuario import Usuario
import os
from proyecto import RegistrarTiqueApp

dao = DAO()
ventana = tk.Tk()
ventana.title("Sistema de Tiques")
ventana.geometry("800x600")

# Definir variables globales para entry_nombre y entry_password
entry_nombre = None
entry_password = None

def mostrar_opciones():
    """Muestra las opciones principales en la ventana.
    
    Esta función crea y muestra los botones para registrar un nuevo usuario 
    e iniciar sesión.
    """
    # Definir y colocar los widgets necesarios
    label_opciones = tk.Label(ventana, text="¿Qué quieres hacer?")
    label_opciones.pack(pady=10)

    # Botón para registrar un nuevo usuario
    btn_registrar = tk.Button(ventana, text="Registrar", command=mostrar_formulario_registrar)
    btn_registrar.pack(pady=5)

    # Botón para iniciar sesión
    btn_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", command=mostrar_formulario_iniciar_sesion)
    btn_iniciar_sesion.pack(pady=5)

def mostrar_formulario_registrar():
    """Muestra el formulario para registrar un nuevo usuario.
    
    Esta función limpia la ventana y coloca los widgets necesarios para 
    registrar un nuevo usuario, incluyendo entradas de nombre, contraseña 
    y selección de rol.
    """
    global entry_nombre, entry_password
    limpiar_ventana()

    # Definir y colocar los widgets necesarios para registrar un nuevo usuario
    label_nombre = tk.Label(ventana, text="Nombre:")
    label_nombre.pack(pady=5)

    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack(pady=5)

    label_password = tk.Label(ventana, text="Contraseña:")
    label_password.pack(pady=5)

    entry_password = tk.Entry(ventana, show="*")  # Campo de contraseña oculta
    entry_password.pack(pady=5)

    # Etiqueta y menú desplegable para seleccionar el rol
    label_rol = tk.Label(ventana, text="Rol:")
    label_rol.pack(pady=5)

    opciones_roles = ["Usuario Común", "Jefe de Mesa", "Ejecutivo"]
    rol_seleccionado = tk.StringVar()
    rol_seleccionado.set(opciones_roles[0])  # Establecer el valor predeterminado
    combo_rol = ttk.Combobox(ventana, values=opciones_roles, textvariable=rol_seleccionado)
    combo_rol.pack(pady=5)

    # Botón para registrar un nuevo usuario
    btn_registrar = tk.Button(ventana, text="Registrar", command=lambda: registrar_usuario(entry_nombre.get(), entry_password.get(), combo_rol.get()))
    btn_registrar.pack(pady=10)

def mostrar_formulario_iniciar_sesion():
    """
    Muestra el formulario para iniciar sesión.
    
    Esta función limpia la ventana y coloca los widgets necesarios para 
    iniciar sesión, incluyendo entradas de nombre y contraseña.
    """
    global entry_nombre, entry_password
    limpiar_ventana()

    # Definir y colocar los widgets necesarios para iniciar sesión
    label_nombre = tk.Label(ventana, text="Nombre:")
    label_nombre.pack(pady=5)

    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack(pady=5)

    label_password = tk.Label(ventana, text="Contraseña:")
    label_password.pack(pady=5)

    entry_password = tk.Entry(ventana, show="*")  # Campo de contraseña oculta
    entry_password.pack(pady=5)

    # Botón para iniciar sesión
    btn_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", command=lambda: iniciar_sesion(entry_nombre.get(), entry_password.get()))
    btn_iniciar_sesion.pack(pady=10)

def limpiar_ventana():
    """
    Limpia todos los widgets de la ventana.
    
    Esta función elimina todos los widgets actuales de la ventana para 
    permitir la visualización de nuevos formularios u opciones.
    """
    for widget in ventana.winfo_children():
        widget.pack_forget()

def registrar_usuario(nombre, contrasenia, rol_elegido):
    """
    Registra un nuevo usuario en el sistema.
    
    Args:
        nombre (str): Nombre del usuario.
        contrasenia (str): Contraseña del usuario.
        rol_elegido (str): Rol seleccionado para el usuario.
    
    Esta función valida los campos de entrada, crea un nuevo objeto Usuario y 
    lo registra en la base de datos. Muestra un mensaje de éxito o error según 
    corresponda.
    """
    # Obtener el ID del rol seleccionado
    if rol_elegido == "Usuario Común":
        rol_id = 1
    elif rol_elegido == "Jefe de Mesa":
        rol_id = 2
    elif rol_elegido == "Ejecutivo":
        rol_id = 3
    else:
        # Si ocurre algún error inesperado, mostrar un mensaje y detener el registro.
        messagebox.showerror("Error", "Rol inválido")
        return

    # Validar que los campos no estén vacíos
    if nombre == "" or contrasenia == "":
        messagebox.showerror("Error", "Nombre y contraseña son requeridos")
        return

    # Crear un nuevo objeto Usuario
    usuario = Usuario(id_usuario=None, nombre_usuario=nombre, contrasenia=contrasenia, rol_id=rol_id)

    # Registrar el usuario en la base de datos
    dao.registrar_usuario(usuario)

    # Mostrar mensaje de éxito
    messagebox.showinfo("Registro exitoso", "El usuario ha sido registrado correctamente")

    # Volver a mostrar las opciones para que el usuario pueda decidir si quiere registrar o iniciar sesión nuevamente
    mostrar_opciones()

def iniciar_sesion(nombre, contrasenia):
    """
    Inicia sesión en el sistema.
    
    Args:
        nombre (str): Nombre del usuario.
        contrasenia (str): Contraseña del usuario.
    
    Esta función valida los campos de entrada, verifica las credenciales del 
    usuario en la base de datos y, si son correctas, inicia la aplicación 
    principal. Muestra un mensaje de éxito o error según corresponda.
    """
    # Validar que los campos no estén vacíos
    if nombre == "" or contrasenia == "":
        messagebox.showerror("Error", "Nombre y contraseña son requeridos")
        return

    # Verificar las credenciales del usuario en la base de datos
    usuario = dao.verificar_credenciales(nombre, contrasenia)
    if usuario:
        # Mostrar mensaje de éxito
        messagebox.showinfo("Inicio de sesión exitoso", "Bienvenido al sistema")

        # Cerrar la ventana actual de inicio de sesión
        ventana.destroy()

        root = tk.Tk()
        app = RegistrarTiqueApp(root)
        root.mainloop()
    
    else:
        messagebox.showerror("Inicio de sesión fallido", "Credenciales incorrectas")

    # Limpiar los campos de entrada
    entry_nombre.delete(0, "end")
    entry_password.delete(0, "end")



# Mostrar las opciones al iniciar la aplicación
mostrar_opciones()

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
