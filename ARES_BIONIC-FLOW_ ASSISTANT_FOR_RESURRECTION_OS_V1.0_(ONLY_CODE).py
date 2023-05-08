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
import platform
import urllib.error
import winreg
import psutil
import wmi
import tempfile


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
        8. Descargar / Instalar Lively Wallpaper (sólo para Resurrection OS Full y Full 
        Legends)
        9. Descargar / Instalar 7-Zip
        10. Descargar / Instalar IDM (Internet Download Manager)
        11. Descargar / Instalar Microsoft PowerToys (sólo Resurrection OS compatibles)
        12. Regresar al menú principal
        -----------------------------------------------------------------------------------
"""
print(menú_opción_1)
opcion_menu_opción_1_menu_principal = input("¿Qué deseas hacer?: ")
### DESCARGA E INSTALACIÓN DE GOOGLE CHROME ###
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
        print(menú_opción_1)
    else:
        print("De acuerdo. Regresando al menú principal...")
        time.sleep(3)
        os.system("cls")
        print(menú_opción_1)
elif opcion_menu_opción_1_menu_principal == "2":
    confirmación_2 = input("¿Deseas instalar Microsoft Edge? (S/N): ")
    if confirmación_2.upper() == "S":
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
        print(menú_opción_1)
    else:
        print("De acuerdo. Regresando al menú principal...")
        time.sleep(3)
        print(menú_opción_1)
### DESCARGA E INSTALACIÓN DE MOZILLA FIREFOX ###
elif opcion_menu_opción_1_menu_principal == "3":
    confirmación_3 = input("¿Deseas descargar Mozilla Firefox? (S/N): ")
    if confirmación_3.upper() == "S":
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
        print(menú_opción_1)
    else:
        print("De acuerdo. Regresando al menú principal...")
        time.sleep(3)
        os.system("cls")
        print(menú_opción_1)
elif opcion_menu_opción_1_menu_principal == "4":
    confirmación_4 = input("¿Deseas instalar LibreWolf? (S/N): ")
    if confirmación_4.upper() == "S":
        print("¡Entendido! Descargando LibreWolf...")
        url = "https://gitlab.com/api/v4/projects/44042130/packages/generic/librewolf/112.0.2-1/librewolf-112.0.2.1-windows-x86_64-setup.exe"
        subprocess.call(["powershell.exe, -Command", "f(New-Object System.Net.WebClient).DownloadFile('{url}', 'LibreWolfInstaller.exe')"])
        print("¡Listo! LibreWolf descargado. Instalando ahora...")
        subprocess.call(["LibreWolfInstaller.exe", "/S"])
        print("¡Listo! LibreWolf instalado. Ve al Escritorio para comprobarlo :)")
        subprocess.call('cls', shell=True)
    else:
        print("De acuerdo. Regresando al menú principal...")
        time.sleep(3)
        os.system("cls")
        print(menú_opción_1)
elif opcion_menu_opción_1_menu_principal == "5":
    confirmación_5 = input("¿Deseas instalar VLC Media Player? (S/N): ")
    if confirmación_5.upper() == "S":
        print("¡De acuerdo! Descargando VLC Media Player...")
        url = "https://get.videolan.org/vlc/3.0.16/win32/vlc-3.0.16-win32.exe"
        try:
            urllib.request.urlretrieve(url, "vlc.exe")
        except:
            print("¡Oops! Hubo un error al intentar descargar VLC Media Player. ¡Inténtalo nuevamente!")
            os.system("cls")
            print(menú_opción_1)
    elif():
        print("¡Listo! VLC Media Player descargado. Instalando ahora...")
        os.system('vlc.exe /L=1034 /S')
        print("¡Listo! VLC Media Player instalado. Compruébalo en el Menú Inicio o el Escritorio :)")
        time.sleep(5)
        os.system('cls')
        print(menú_opción_1)
    else:
        print("De acuerdo. Regresando al menú principal...")
        time.sleep(3)
        os.system('cls')
        print(menú_opción_1)
elif opcion_menu_opción_1_menu_principal == "6":
    confirmación_6 = input("¡Buena elección! ¿Deseas instalar K-Lite Codec Pack? (S/N): ")
    if confirmación_6.upper() == "S":
        print("¡Entendido! Descargando K-Lite Codec Pack...")
        url = "https://files3.codecguide.com/K-Lite_Codec_Pack_1605_Full.exe"
        filename = "K-Lite_Codec_Pack_1605_Full.exe"
        descargar_instalador = (url, filename)
        print("¡Listo! K-Lite Codec Pack descargado. Instalando ahora...")
        silent_install = (filename)
        print("¡Listo! K-Lite Codec Pack instalado. Ve al Menú Inicio y compruébalo; ¡disfruta de tus vídeos como nunca!")
        os.system('cls')
        print(menú_opción_1)
    else:
        print("De acuerdo. Regresando al menú anterior...")
        time.sleep(3)
        os.system("cls")
        print(menú_opción_1)
elif opcion_menu_opción_1_menu_principal == "7":
confirmación_7 = input("¡Excelente! ¿Deseas instalar Rainmeter?\n NOTA: Asegúrate de que tu PC cumple con los requisitos ;) (S/N): ")
if confirmación_7.upper() == "S":
    print("\n¡Entendido! Antes de instalar Rainmeter, para ofrecerte la mejor experiencia y evitar deficiencias en el rendimiento, realizaré una comprobación rápida en tu equipo, para asegurarme que cumples con los requisitos de Rainmeter, y los recomendados para Resurrection OS.")
    print("\n Comprobando si cumples con los requisitos...")
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\OEMInformation") as key:
            oem_info = winreg.QueryValueEx(key, "Model")[0]
    except:
            oem_info = ""
            os_version = platform.release()
            cpu_info = psutil.cpu_freq().max / 1000
            ram_info = psutil.virtual_memory().total / (1024 ** 3)
if ("Full" in oem_info or "Full Legends" in oem_info) and cpu_info >= 2 and ram_info >=2:
    print("\n¡Felicidades, cumples con los requisitos! Descargando Rainmeter...")
    url = "https://github.com/rainmeter/rainmeter/releases/download/v.4.4.0.3518/Rainmeter-4.4-r3518-beta.exe"
    filename = "Rainmeter.exe"
    try:
        urllib.request.urlretrieve(url, filename)
    except urllib.error.URLError:
        print("\n¡Oh no! Ocurrió un error al descargar Rainmeter. ¡Reingresa aquí desde el menú anterior e inténtalo nuevamente!")
        time.sleep(5)
        os.system("cls")
        print(opcion_menu_opción_1_menu_principal)
    print("n\¡Listo! Rainmeter descargado. Instalando ahora...")
    os.system("start /wait " + filename + " /S")
    print("\n¡Listo! Rainmeter instalado. Ve al Menú Inicio y compruébalo :)")
    time.sleep(5)
    os.system("cls")
    print(menú_opción_1)
elif "Full" in oem_info or "Full Legends" in oem_info:
    print("\nEspera... algo no cuadra bien aquí... \n")
    print("¿Qué es lo que no cuadra?...\n")
    print("Estás intentando instalar Rainmeter en un equipo donde tienes instalado Resurrection OS Full o Full Legends, pero que no cumple con los requisitos mínimos de Rainmeter:\n- Sistema operativo de Windows 7 en adelante. \n- Un equipo con mínimo 2 GHz de procesador (recomendado).\n-2 GB de RAM, para un buen rendimiento (recomendado).\n¡Ten mucho cuidado! Aunque Rainmeter por sí solo no es muy pesado, puede llegar a serlo dependiendo de la skin que escojas, y puede desembocar en problemas de rendimiento si usas una skin muy detallada o con demasiados elementos. Puedo instalarlo por ti de todas maneras si lo prefieres, pero si surgen problemas de rendimiento, mi creador no se responsabiliza. ¿Deseas que lo instalemos de todas formas? (S/N)\n")
    instalar = input()
    if instalar.upper == "S":
        print("\nEntiendo. Instalaré Rainmeter para ti. Comenzando la descarga...")
        url = "https://github.com/rainmeter/rainmeter/releases/download/v.4.4.0.3518/Rainmeter-4.4-r3518-beta.exe"
        filename = "Rainmeter.exe"
        try:
            urllib.request.urlretrieve(url, filename)
        except urllib.error.URLError:
            print("\n¡Oh no! Ocurrió un error al descargar Rainmeter. ¡Reingresa aquí desde el menú anterior e inténtalo nuevamente!")
            time.sleep(5)
            os.system("cls")
            print(opcion_menu_opción_1_menu_principal)
        print("n\¡Listo! Rainmeter descargado. Instalando ahora...")
        os.system("start /wait " + filename + " /S")
        print("\n¡Listo! Rainmeter instalado. Ve al Menú Inicio y compruébalo :)")
        time.sleep(5)
        os.system("cls")
elif ("Full" in oem_info or "Full Legends" in oem_info) and cpu_info <= 2 and ram_info <=2:
    print("\nEspera... algo no cuadra bien aquí... \n")
    print("¿Qué es lo que no cuadra?...\n")
    print("Estás intentando instalar Rainmeter en un equipo donde tienes instalado Resurrection OS Go o Go Ultra, y de paso, que no cumple con los requisitos mínimos de Rainmeter:\n- Sistema operativo de Windows 7 en adelante. \n- Un equipo con mínimo 2 GHz de procesador (recomendado).\n-2 GB de RAM, para un buen rendimiento (recomendado).\n¡Ten mucho cuidado! Aunque Rainmeter por sí solo no es muy pesado, puede llegar a serlo dependiendo de la skin que escojas, y puede desembocar en problemas de rendimiento si usas una skin muy detallada o con demasiados elementos. Puedo instalarlo por ti de todas maneras si lo prefieres, pero si surgen problemas de rendimiento, mi creador no se responsabiliza. ¿Deseas que lo instalemos de todas formas? (S/N)\n")
    instalar_2 = input()
    if instalar_2.upper == "S":
        print("\nEntiendo. Instalaré Rainmeter para ti. Comenzando la descarga...")
        url = "https://github.com/rainmeter/rainmeter/releases/download/v.4.4.0.3518/Rainmeter-4.4-r3518-beta.exe"
        filename = "Rainmeter.exe"
        try:
                urllib.request.urlretrieve(url, filename)
        except urllib.error.URLError:
            print("\n¡Oh no! Ocurrió un error al descargar Rainmeter. ¡Reingresa aquí desde el menú anterior e inténtalo nuevamente!")
            time.sleep(5)
            os.system("cls")
            print(opcion_menu_opción_1_menu_principal)
        print("n\¡Listo! Rainmeter descargado. Instalando ahora...")
        os.system("start /wait " + filename + " /S")
        print("\n¡Listo! Rainmeter instalado. Ve al Menú Inicio y compruébalo :)")
        time.sleep(5)
        os.system("cls")
    else:
        print("\nEntendido. Regresando al menú principal...")
        os.system("cls")
        print(opcion_menu_opción_1_menu_principal)
elif (opcion_menu_opción_1_menu_principal) == "9":
    confirmacion_9 = input("¿Deseas instalar 7-Zip? (S/N): ")
    if confirmacion_9.upper() == "S":
        print("Descargando 7-Zip...")
        url = "https://7-zip.org/a/7z2201-x64.exe"
        file_name = "7z2201-x64.exe"
        response = requests.get(url, stream=True)
        with open(file_name, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print("7-Zip descargado. Instalando ahora...")
        subprocess.run([file_name, "/S"])
        print("7-Zip instalado. Ve al Menú Inicio y compruébalo :)")
        time.sleep(5)
        os.system("cls")
        print(opcion_menu_opción_1_menu_principal)
    else:
        print("De acuerdo. Regresando al menú principal...")
        time.sleep(3)
        os.system("cls")
        print("menu_opcion_1")
elif opcion_menu_opción_1_menu_principal == "10":
    confirmacion_10 = input("¿Deseas instalar IDM (Internet Download Manager)? (S/N): ")
    if confirmacion_10.upper() == "S":
        print("Descargando IDM...")
        url = "https://mirror2.internetdownloadmanager.com/idman641build11.exe?v=lt&filename=idman641build11.exe"
        file_name = "idman641build11.exe"
        response = requests.get(url, stream=True)
        with open(file_name, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print("IDM descargado. Instalando ahora...")
        command = f'start /wait "" {file_name} /silent'
        subprocess.run(command, shell=True)
        print("IDM instalado. Recuerda: si instalaste IDM teniendo los navegadores abiertos, recuerda reiniciarlos, así IDM termina de instalarse.\n")
        print("Aunque puedes dejarlos abiertos de todas maneras; en unos segundos en tu navegador aparecerá una alerta preguntándote si deseas habilitar la extensión 'IDM Integration Module'\n")
        print("Pulsa en 'Habilitar extensión' y si te aparece 'IDM Integration Module for {el nombre de tu navegador} has been installed.', ¡ya estás listo para usar IDM!\n")
        print("Si deseas acceder a IDM, puedes hacerlo desde el menú Inicio o desde el Escritorio.")
        print("Una cosa más: recuerda activarlo. Si quieres bajar la versión crackeada, puedes usar este link (recuerda usar AdBlock): https://descarga.xyz/internet-download-manager-full-crack/.")
        print("¡Disfruta tus descargas ahora más rápidas!")
        time.sleep(7)
        os.system("cls")
        print(menú_opción_1)
    else:
        print("De acuerdo. Si cambias de opinión, selecciona la opción de IDM en el menú de descarga e instalación de programas. Regresando al menú principal...")
        time.sleep(5)
        os.system("cls")
        print(menú_opción_1)
elif opcion_menu_opción_1_menu_principal == "11":
    print("¡Bien! Has elegido instalar Microsoft PowerToys.")
    confirmación_11 = input("¿Deseas continuar con la instalación? (S/N): ")
    if confirmación_11.upper() == "S":
        print("¡Entendido! Antes de instalar Microsoft PowerToys en tu equipo, deberé realizar una comprobación rápida en tu equipo, para saber si cumple con los requisitos de Microsoft PowerToys.")
        print("Comprobando si tu equipo cumple con los requisitos...")
        info_sistema = platform.uname()
        if info_sistema.system == "Windows" and (info_sistema.release.startswith("10.")and int(info_sistema.release.split(".")[2]) >= 19041) or info_sistema.release.startswith("11.") and info_sistema.machine in ["AMD64, arm64"]:
            print("¡Felicidades, tu equipo cumple con los requisitos! Ahora bien, ¿deseas instalar Microsoft PowerToys en tu equipo? (S/N): ")
            confirmación_11_1 = input()
            if confirmación_11_1.upper() == "S":
                print("¡Entendido! Descargando Microsoft PowerToys...")
                url = "https://github.com/microsoft/PowerToys/releases/download/v0.69.1/PowerToysSetup-0.69.1-x64.exe"
                nombre_archivo = url.split("/")[-1]
                response = requests.get(url, stream=True)
                with open(nombre_archivo, "wb") as f:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                print("¡Hecho! Microsoft PowerToys descargado. Instalando ahora...")
                os.system(f'start /wait "" "{nombre_archivo}" /S /D=C:\PowerToys')
                print("¡Hecho! Microsoft PowerToys instalado. ¡Disfruta personalizando tu equipo!")
                time.sleep(5)
                os.system("cls")
                print(menú_opción_1)
            else:
                os.system("cls")
        else:
            print("¡Oh, vaya! Algo ha pasado. \nEsto fue lo que pasó: Lo siento, no puedo instalar Microsoft PowerToys en tu equipo ya que éste no cumple con sus requisitos. \nSistemas operativos admitidos:\nWindows 11 (21H2 y 22H2)\nWindows 10 v2004 (compilación 19041) o posterior\nArquitectura del sistema: Actualmente, se admiten las arquitecturas x64 y ARM64. No puedo ofrecerte la instalación de todas maneras, ya que si lo intento, el instalador de todas maneras arrojará error de incompatibilidad. Por favor, asegúrate de tener una edición de Resurrection OS instalada que esté basada en alguna de las versiones de Windows compatibles con PowerToys e inténtalo de nuevo. ¡Disculpa los inconvenientes!")
            input("Presiona cualquier tecla para regresar al menú anterior...")
            os.system("cls")
    else:
        print("De acuerdo. Regresando al menú anterior...")
        time.sleep(3)
        os.system("cls")
        print(menú_opción_1)
elif opcion_menu_opción_1_menu_principal == "12":
    print("Regresando al menú principal...")
    time.sleep(3)
    os.system("cls")
    print(menú_principal)
else:
    print("¡Lo siento! Tu opción no es válida. ¡Ingresa una opción válida!")
    input("Presiona cualquier tecla...")

### OPCIÓN 2 (CONFIGURAR LA PERSONALIZACIÓN)

def imprimir_menú_opción_2():
    os.system('cls' if os.name == 'nt' else 'clear')

menú_opción_2 = """
        ------------------------------------------------------------------------------------
        |                                                                                  |
        |                           CONFIGURAR LA PERSONALIZACIÓN                          |
        |                                                                                  |
        ------------------------------------------------------------------------------------
        1. Activar el modo oscuro o claro para todas las aplicaciones (sólo Resurrection OS
        10 y 11)
        2. Cambiar la orientación de la barra de tareas (sólo Resurrection OS 11)
        3. Activar/Desactivar efectos de transparencia
        4. Cambiar el color de énfasis del sistema
        5. Aplicar los temas para Windows oficiales de Resurrection OS
        6. Desactivar Mostrar sugerencias ocasionalmente en Inicio
        7. Cambiar fuente del sistema
        8. Instalar skin de Rainmeter (¡úsalo sólo si tienes Rainmeter instalado!)
        8. Regresar al menú principal
        -----------------------------------------------------------------------------------
"""
print(menú_opción_2)
opcion_menu_opción_2_menu_principal = input("¿Qué deseas hacer?: ")

### ACTIVAR EL MODO OSCURO O CLARO PARA TODAS LAS APLICACIONES ###

def obtener_modo_color_actual():
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize") as key:
        value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        return "Claro" if value else "Oscuro"

if opcion_menu_opción_2_menu_principal == "1":
    os.system("cls")
    modo_actual = obtener_modo_color_actual()
opcion_1_menu_opcion_2 = """
        ------------------------------------------------------------------------------------
        |                                                                                  |
        |           ACTIVAR EL MODO OSCURO O CLARO PARA TODAS LAS APLICACIONES             |
        |                                                                                  |
        ------------------------------------------------------------------------------------
        Tu tema de color del sistema actual: {modo_actual}
        1. Cambiar a modo Claro
        2. Cambiar a modo Oscuro
        3. Regresar al menú anterior
        ------------------------------------------------------------------------------------
""" 
opcion = input("Escoge el número del modo al que deseas cambiar: ")
if opcion == "1" and modo_actual == "Oscuro":
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", 0, winreg.KEY_WRITE) as key:
        winreg.SetValueEx(key, "AppsUseLightTheme", 0, winreg.REG_DWORD, 1)
    print("¡Modo claro Activado!")
    time.sleep(3)
    os.system("cls")
    print(opcion_1_menu_opcion_2)
elif opcion == "2" and modo_actual == "Claro":
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\CurrentVersion\Themes\Personalize", 0, winreg.KEY_WRITE) as key:
        winreg.SetValueEx(key, "AppsUseLightTheme", 0, winreg.REG_DWORD, 0)
    print("¡Modo Oscuro activado!")
elif opcion == "1" and modo_actual == "Claro":
    print("¡Ya estás en modo claro!")
    input("Presiona cualquier tecla para refrescar el menú...")
elif opcion == "2" and modo_actual == "Oscuro":
    print("¡Ya estás en modo oscuro!")
    input("Presiona cualquier tecla para refrescar el menú...")
elif opcion == "3":
    print("De acuerdo. Regresando al menú anterior...")
    time.sleep(3)
    os.system("cls")
    print(menú_opción_2)





    


        



    

