'''ESTE SCRIPT NOS MOSTRARÁ TODAS LAS APLICACIONES QUE
TENGAMOS INSTALADAS EN EL SISTEMA CON SOLO EJECUTAR.'''


import winreg
import tkinter as tk

# ESTE SCRIPT NOS MOSTRARÁ TODAS LAS APLICACIONES QUE TENGAMOS
# INSTALADAS EN EL SISTEMA CON SOLO EJECUTAR.

def get_installed_applications():
    app_list = []    # LISTA PARA ALMACENAR LAS APLICACIONES INSTALADAS

    uninstall_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
    # DEFINIR LA RUTA DE LA CLAVE DE REGISTRO DONDE SE ALMACENAN LAS APLICACIONES INSTALADAS.
    # EN ESTE CASO, SE TRATA DE LA CLAVE 'Uninstall' BAJO 'CurrentVersion' EN EL REGISTRO DE WINDOWS.

    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, uninstall_key) as key:
        # ABRIR LA CLAVE DE REGISTRO ESPECIFICADA UTILIZANDO LA FUNCIÓN 'OpenKey' DEL MÓDULO 'winreg'.
        # EN ESTE CASO, SE ABRE LA CLAVE EN MODO DE SOLO LECTURA.

        # RECORRER LAS SUBCLAVES DEL REGISTRO
        for i in range(winreg.QueryInfoKey(key)[0]):
            # ITERAR SOBRE LAS SUBCLAVES DE LA CLAVE DE REGISTRO UTILIZANDO UN BUCLE 'for' Y LA FUNCIÓN 'EnumKey'.
            # 'QueryInfoKey' DEVUELVE INFORMACIÓN SOBRE LA CLAVE DE REGISTRO, SIENDO EL PRIMER ELEMENTO EL NÚMERO DE SUBCLAVES.

            subkey_name = winreg.EnumKey(key, i)
            # OBTENER EL NOMBRE DE LA SUBCLAVE EN LA POSICIÓN 'i' UTILIZANDO LA FUNCIÓN 'EnumKey' DEL MÓDULO 'winreg'.

            subkey_path = fr"{uninstall_key}\{subkey_name}"
            # CONSTRUIR LA RUTA COMPLETA DE LA SUBCLAVE CONCATENANDO LA RUTA DE LA CLAVE 'Uninstall' Y EL NOMBRE DE LA SUBCLAVE.

            # OBTENER EL NOMBRE DE LA APLICACIÓN Y AGREGARLO A LA LISTA
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path) as subkey:
                # ABRIR LA SUBCLAVE DE REGISTRO UTILIZANDO LA FUNCIÓN 'OpenKey' DEL MÓDULO 'winreg'.
                # EN ESTE CASO, SE ABRE EN MODO DE SOLO LECTURA.

                try:
                    app_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                    # OBTENER EL VALOR DE LA ENTRADA DE REGISTRO "DisplayName" UTILIZANDO LA FUNCIÓN 'QueryValueEx'.
                    # ESTO DEVUELVE EL NOMBRE DE LA APLICACIÓN INSTALADA.

                    app_list.append(app_name)
                    # AGREGAR EL NOMBRE DE LA APLICACIÓN A LA LISTA 'app_list'.

                except OSError:
                    pass                      # SI OCURRE UNA EXCEPCIÓN DE TIPO 'OSError'
    return app_list                           # DEVOLVER LA LISTA DE APLICACIONES INSTALADAS.
   

applications = get_installed_applications()   # LLAMAR A LA FUNCIÓN 'get_installed_applications' PARA OBTENER LA LISTA DE APLICACIONES INSTALADAS.

#MOSTRAR LA LISTA DE APLICACIONES EN UNA VENTANA DE TKINTER
# CREAR LA VENTANA PRINCIPAL
window = tk.Tk()
window.title("BUSCADOR DE PROGRAMAS                      ÐɮŌ 🤸‍♀️")
window.geometry("480x330")
title_font = ("Arial", 15, "bold")

# CREAR UN SCROLLBAR
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# CREAR UN WIDGET DE ETIQUETA PARA ALMACENAR LA INFORMACIÓN
label = tk.Label(window, text="PROGRAMAS INSTALADOS EN TU PC:", font=("Arial", 12, "bold italic"), fg="black")
label.pack()

# CREAR UN WIDGET DE CUADRO DE TEXTO CON SCROLLBAR
text_box = tk.Text(window, font=("Arial", 10), fg="black", yscrollcommand=scrollbar.set)
text_box.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=text_box.yview)

# INSERTAR LOS DATOS DE LAS APLICACIONES EN EL CUADRO DE TEXTO
for i, app in enumerate(applications):
    text_box.insert(tk.END, f"{i+1}. {app}\n")

# EJECUTAR EL BUCLE PRINCIPAL DE TKINTER
window.mainloop()


