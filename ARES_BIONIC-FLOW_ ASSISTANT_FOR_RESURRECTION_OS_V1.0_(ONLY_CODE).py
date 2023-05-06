### COMIENZO DEL SCRIPT ARES BIONIC-FLOW BOT ASSISTANT FOR RESURRECTION OS, VERSIÓN 1.0 ###

### IMPORTACIÓN DE LIBRERÍAS NECESARIAS ###
import subprocess
import ctypes as ct
import time
import textwrap
import sys
import os
import urllib.request
import requests

### CAMBIAR TÍTULO DE LA CONSOLA DE COMANDOS (CMD) ###
ct.windll.kernel32.SetConsoleTitleW("ARES Bionic-Flow Bot Assistant for Resurrection OS, v1.0")

### FUNCIÓN PARA IMPRIMIR EL RECUADRO ASCII, CENTRANDO EL MENSAJE ###
def imprimir_mensaje_en_recuadro(mensaje):
    width = 60
    lines = textwrap.wrap(mensaje, width=width-4)
    box_top = '+' + '-'*(width-2) + '+'
    box_middle = '| {0:^{1}} |'
    box_bottom = '+' + '-'*(width-2) + '+'

    print(box_top)
    for line in lines:
        print(box_middle.format(line, width-4))
    print(box_bottom)

### VERIFICAR SI SE EJECUTA COMO ADMINISTRADOR ###
def es_administrador():
    try:
        return ct.windll.shell32.IsUserAnAdmin()
    except:
        return False

if es_administrador():
    print("---- BIENVENIDO AL ARES BIONIC-FLOW BOT ASSISTANT FOR RESURRECTION OS v1.0 ----")
    mensaje = "¡Hola! Te doy la bienvenida. Soy ARES Bionic-Flow, el script tipo bot automatizado oficial de Resurrection OS, y estoy aquí para ayudarte a dar tus primeros pasos con Resurrection OS, o ayudarte mientras lo usas. Mis tareas son: ayudarte a descargar e instalar software más fácilmente, configurar por ti ciertos perfiles de personalización en el sistema, ayudarte a optimizarlo en casos de emergencia, habilitar algunos útiles en el sistema, entre otras cosas. Cabe aclararte que, en mi menú principal, luego de esta pantalla, habrá una opción que te permitirá habilitar la Protección del sistema (en caso de que no la tengas activada) y crear un punto de restauración, en caso de que alguna de las cosas que realizo cause algún daño en el sistema. ¡Estoy aquí para ayudarte! Si me necesitas, abre el Menú Extendido de Resurrection OS y allí me encontrarás. Dale a la opción 'Iniciar ARES Bionic-Flow Bot'"
    imprimir_mensaje_en_recuadro(mensaje)
else:
    print("¡Oh no! Algo ha pasado. :(\n\nEsto pasó: No me has ejecutado como Administrador. ¡No puedo funcionar correctamente si no me ejecutas con privilegios de Administrador! Ya que muchas de las cosas que hago requieren realizar cambios en el sistema, que requieren de aprobación. \nPor favor, cierra esta ventana y ejecútame nuevamente, pero dando en la opción 'Ejecutar como Administrador', e intenta nuevamente. .\n\n¡Espero verte por acá de nuevo! Recuerda ejecutarme como Administrador.")

respuesta = input("¿Estás listo para comenzar? (S/N): ")

if respuesta.upper() == 'S':
    print("\n¡Perfecto! ¡Comencemos!")
    time.sleep(5)
elif respuesta.upper() == 'N':
    print("\n¡Nos vemos! Recuerda: si me necesitas, me puedes encontrar en el Menú Extendido de Resurrection OS, haciendo clic en la opción 'Iniciar ARES Bionic-Flow Bot. ¡Te veo luego!")
    time.sleep(5)
    exit()
else:
    print("¡Lo siento! Tu opción no es válida. Intenta nuevamente.")

    

### OPCIONES DEL MENÚ PRINCIPAL ###

### MOSTRAR EL MENÚ PRINCIPAL ###
menú_principal = """
        ------------------------------------------------------
        |                   MENÚ PRINCIPAL                   |
        ------------------------------------------------------
        | 1. Descarga / Instalación de software/programas    |
        | 2. Configurar la personalización                   |
        | 3. Optimización del sistema                        |
        | 4. Activación de parámetros útiles                 |
        | 5. Salir                                           |
        ------------------------------------------------------
        """
print(menú_principal)
opción = input("¿Qué opción deseas elegir?: ")
if opción == "1":
    print("Bien. Opción 1.")
elif opción == "2":
    print("Ok. Opción 2.")
elif opción == "3":
    print("¡Bien! Opción 3.")
elif opción == "4":
    print("¡De acuerdo! Opción 4.")
elif opción == "5":
    print("\n¡Nos vemos! Recuerda: si me necesitas, me puedes encontrar en el Menú Extendido de Resurrection OS, haciendo clic en la opción 'Iniciar ARES Bionic-Flow Bot. ¡Te veo luego!")
    time.sleep(5)
    exit()
else:
    print("¡Lo siento! Tu opción no es válida.")

### FUNCIÓN PARA IMPRIMIR EL MENÚ DE LA OPCIÓN 1 ###
def imprimir_menú():
    os.system('cls' if os.name == 'nt' else 'clear')

menú_opción_1 = """
        ------------------------------------------------------------------------------------
        |                                                                                  |
        |                           DESCARGA / INSTALACIÓN DE PROGRAMAS                    |
        |                                                                                  |
        ------------------------------------------------------------------------------------
        1. Descargar / Instalar Google Chrome
        2. Descargar / Instalar Microsoft Edge
        3. Descargar / Instalar Mozilla Firefox
        4. Descargar / Instalar LibreWolf
        5. Descargar / Instalar VLC Media Player
        6. Descargar / Instalar K-Lite Codec Pack
        7. Descargar / Instalar Rainmeter (sólo para Resurrection OS Full y Full Legends)
        8. Descargar / Instalar Lively Wallpaper
        9. Descargar / Instalar 7-Zip
        10. Descargar / Instalar IDM (Internet Download Manager)
        11. Descargar / Instalar Microsoft PowerToys
        12. Regresar al menú principal
        -----------------------------------------------------------------------------------
"""
print(menú_opción_1)
opcion_menu_opción_1_menu_principal = input("¿Qué deseas hacer?: ")
if opcion_menu_opción_1_menu_principal == "1":
    confirmación = input("¿Deseas instalar Google Chrome? (S/N): ")
    if confirmación.upper() == "S":
        print("\n")
        print("¡Entendido! Descargando Google Chrome...")
        url = "https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B22E08B62-68D8-F2E3-BC3B-1CBE9EE0FCE1%7D%26lang%3Den%26browser%3D5%26usagestat%3D0%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_0%26brand%3DGCEA/dl/chrome/install/GoogleChromeStandaloneEnterprise64.msi"
        filename = "GoogleChromeStandaloneEnterprise64.msi"
        urllib.request.urlretrieve(url, filename)
        print("¡Listo! Google Chrome descargado. Instalando ahora...")
        os.system(f'msiexec /i {filename} /quiet /qn /norestart')
        print("¡Listo! Google Chrome instalado. Ve al Escritorio para comprobarlo :)")
        time.sleep(5)
        os.system("cls")
        print(opcion_menu_opción_1_menu_principal)
elif opcion_menu_opción_1_menu_principal == "2":
    print("\n")
    print("¡Entendido! Descargando Microsoft Edge...")
    url = 'https://go.microsoft.com/fwlink/?linkid=2108834'
    filename = 'MicrosoftEdgeSetup.exe'
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
    print("¡Listo! Microsoft Edge descargado. Instalando ahora...")
    command = f'{filename} /silent /install'
    print("¡Listo! Microsoft Edge instalado. Ve al Escritorio para comprobarlo :)")
    time.sleep(5)
    os.system("cls")
    print(opcion_menu_opción_1_menu_principal)
elif opcion_menu_opción_1_menu_principal == "3":
    print("\n")
    print("¡Entendido! Descargando Mozilla Firefox...")
    firefox_url = "https://download.mozilla.org/?product=firefox-latest&os=win64&lang=es-ES"
    firefox_installer = os.path.join(tempfile.gettempdir(), "Firefox Setup.exe")
    urllib.request.urlretrieve(firefox_url, firefox_installer)
    print("¡Listo! Mozilla Firefox descargado. Instalando ahora...")
    subprocess.call(firefox_installer + ' /S', shell=True)
    print("¡Listo! Mozilla Firefox instalado. Ve al Escritorio para comprobarlo :)")
    time.sleep(5)
    os.system('cls')
    print(opcion_menu_opción_1_menu_principal)
elif opcion_menu_opción_1_menu_principal == "4":
    print("¡De acuerdo! Descargando VLC Media Player...")
    url = "https://get.videolan.org/vlc/3.0.16/win32/vlc-3.0.16-win32.exe"
    try:
        urllib.request.urlretrieve(url, "vlc.exe")
        except:
            print("¡Oops! Hubo un error al intentar descargar VLC Media Player. ¡Inténtalo nuevamente!")
            os.system("cls")
            print(opcion_menu_opción_1_menu_principal)
        else:
            print("¡Listo! VLC Media Player descargado. Instalando ahora...")
            os.system('vlc.exe /L=1034 /S')
            print("¡Listo! VLC Media Player instalado. Compruébalo en el Menú Inicio o el Escritorio :)")
            time.sleep(5)
            os.system('cls')
            print(opcion_menu_opción_1_menu_principal)
    os.system('cls')
elif opcion_menu_opción_1_menu_principal == "5":
    print("¡Buena elección! ¡Entendido! Descargando K-Lite Codec Pack...")
    url = "https://files3.codecguide.com/K-Lite_Codec_Pack_1605_Full.exe"
    filename = "K-Lite_Codec_Pack_1605_Full.exe"
    descargar_instalador(url, filename)
    print("¡Listo! K-Lite Codec Pack instalado. Ve al Menú Inicio y compruébalo; ¡disfruta de tus vídeos como nunca!")
    os.system('cls')
    print(opcion_menu_opción_1_menu_principal)
elif opcion_menu_opción_1_menu_principal == "6":
    print("\n¡Entendido! Descargando Rainmeter...")
    url = "https://"

