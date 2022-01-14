import time
import subprocess
from mcstatus import MinecraftServer
import re
from colorama import Fore, init
init()
import os
# funciones

def start_server():
	try:
		for i in range(1,11):
			subprocess.call("clear",shell=True)
			print("Iniciando servidor\n[",f"{Fore.GREEN}█"*i,f"{Fore.WHITE}","]","{}% / 100%\nCTRL + C Para cancelar".format(i*10))
			time.sleep(0.2)
			subprocess.call("clear", shell=True)
		
		print("Servidor listo")
		subprocess.call("screen -S server sh iniciar.sh", shell=True)
	except:
		subprocess.call("clear", shell=True)
		print("Cancelado correctamente")
		time.sleep(5)


def close_server():
	select = input("¡Metodo solo de ¡URGENCIA! (cierra el servidor entrando a la consola y poniendo el comando 'stop')\n¿Deseas continuar? [SI/NO]\n...").upper()
	if select == "SI":	
		subprocess.call("screen -S -X server quit",shell=True)
	elif select == "NO":
		print("Saliendo del programa")

def entry_server():
	try:
		subprocess.call("screen -r server",shell=True)
	except:
		print("Servidor ya esta siendo observado")

def eula_sh(ram,jarFile):
	file = open("eula.txt","w")
	file.write("eula=true")	
	file.close()
	file = open("iniciar.sh","w")
	file.write("java -Xmx{}G -Xms{}G -jar {} ".format(ram,ram,jarFile))
	file.close()

"""def change_ram():
	file = open("iniciar.sh","w")
	ram = int(input("Ingrese valor de ram en GB\n..."))
	file.write("{} {}".format(ram,ram))
	file.close()
"""

def download_server():
	options = int(input("[1]Spigot\n[2]Paper\n[3]Purpur\n..."))

	# SPIGOT
	if options == 1:
		
		# Libreria
		versionesSP = {1: "https://download.getbukkit.org/spigot/spigot-1.18.1.jar",2: "https://download.getbukkit.org/spigot/spigot-1.17.1.jar",3: "https://cdn.getbukkit.org/spigot/spigot-1.16.5.jar",4: "https://cdn.getbukkit.org/spigot/spigot-1.15.2.jar",5: "https://cdn.getbukkit.org/spigot/spigot-1.14.4.jar",6: "https://cdn.getbukkit.org/spigot/spigot-1.12.2.jar",7: "https://cdn.getbukkit.org/spigot/spigot-1.8.8-R0.1-SNAPSHOT-latest.jar",}
		versiones_PR = int(input("[1]1.18.1\n[2]1.17.1\n[3]1.16.5\n[4]1.15.2\n[5]1.14.4\n[6]1.12.2\n[7]1.8.8"))
		versiones_FN = versionesSP[versiones_PR]

		# Descarga
		subprocess.call('wget -t 100 {} -O "spigot.jar"'.format(versiones_FN), shell=True)

		# Inicio
		eula_sh(ram = int(input("Ingrese valor de ram en GB\n...")),jarFile = "spigot.jar")
		start_server()

	# PAPER
	elif options == 2:	
		
		# Libreria
		versionesPA = {1: "https://papermc.io/api/v2/projects/paper/versions/1.18.1/builds/140/downloads/paper-1.18.1-140.jar",2: "https://papermc.io/api/v2/projects/paper/versions/1.17.1/builds/408/downloads/paper-1.17.1-408.jar"}
		versiones_PR = int(input("[1]1.18.1\n[2]1.17.1\n..."))
		versiones_FN = versionesPA[versiones_PR]

		# Descarga
		subprocess.call('wget -t 100 {} -O "paper.jar"'.format(versiones_FN), shell=True)

		# Inicio	
		eula_sh(ram = int(input("Ingrese valor de ram en GB\n...")),jarFile = "paper.jar")
		start_server() # inicia el server

	# PURPUR
	elif options == 3:

		# Libreria
		versionesPU = {1:"https://api.purpurmc.org/v2/purpur/1.18.1/1497/download",2:"https://api.purpurmc.org/v2/purpur/1.17.1/1428/download",3:"https://api.purpurmc.org/v2/purpur/1.16.5/1171/download"}
		versiones_PR = int(input("[1]1.18.1\n[2]1.17.1\n[3]1.16.5\n\n..."))
		versiones_FN = versionesPU[versiones_PR]

		# Descarga
		subprocess.call('wget -t 100 {} -O "purpur.jar"'.format(versiones_FN), shell=True)

		# Inicio	
		eula_sh(ram = int(input("Ingrese valor de ram en GB\n...")),jarFile = "purpur.jar")
		start_server() # inicia el server


def changeRam(ram,jarfile):
	file = open("iniciar.sh","w")
	file.write("java -Xmx{}G -Xms{}G -jar {} ".format(ram,ram,jarfile))
	file.close()

def change_ram():
	jarFile = int(input("[1]Spigot\n[2]Paper\n[3]Purpur\n[0]Salir\n..."))

	if jarFile == 1:
		changeRam(ram = int(input("Ingrese valor de ram en GB\n...")),jarfile = "spigot.jar")
	elif jarFile == 2:
		changeRam(ram = int(input("Ingrese valor de ram en GB\n...")),jarfile = "paper.jar")
	elif jarFile == 3:
		changeRam(ram = int(input("Ingrese valor de ram en GB\n...")),jarfile = "purpur.jar")


def pingServerName():
    try:
        serverNamePing = input("Name server [0 For exit]: ")
        if serverNamePing == "0":
        	print("Cerrado correctamente")
        else:
	        server = MinecraftServer.lookup(serverNamePing)
	        status = server.status()
	        response = server.status()
	        print(f"Jugadores: {response.players.online}/{response.players.max} \nDisponibilidad: { response.players.max - response.players.online}")
	        print(f"Latencia: {status.latency}ms")
	        print(f"Version (Puede ser la de bunge): {response.version.name[0:15]} {response.version.name[-6:]}")
	        response.description = re.sub('§[\da-zA-Z]', '', response.description)
	        print(f"Descripcion: {response.description}\nEstado: Activo")
	        
    except:
    	print("Servidor cerrado o en mantenimiento")

def plugins():
	while True:
		dic ={
		1.1:["EssentialsX 2.19.2", "https://github.com/EssentialsX/Essentials/releases/download/2.19.2/EssentialsX-2.19.2.jar"],
		1.2:["Multiverse-Core 4.3.1", "https://dev.bukkit.org/projects/multiverse-core/files/latest"],
		1.4:["ViaVersion 4.1.1", "https://www.spigotmc.org/resources/viaversion.19254/download?version=429596"],
		1.5:["Protocolib 4.7.0", "https://www.spigotmc.org/resources/protocollib.1997/download?version=408253"],
		1.6:["Skript 2.1.2", "https://dev.bukkit.org/projects/skript/files/latest"],
		1.7:["LPC 3.2.0", "https://www.spigotmc.org/resources/lpc-chat-formatter.68965/download?version=383017"],
		1.8:["Multiverse Portals 4.2.1", "https://dev.bukkit.org/projects/multiverse-portals/files/latest"],
		1.9:["Vault 1.7.3", "https://www.spigotmc.org/resources/vault.34315/download?version=344916"],
		1.11:["Jobs Reborn 5.0.1.0", "https://www.spigotmc.org/resources/jobs-reborn.4216/download?version=428750"],
		1.12:["Dynmap® v3.3-beta-4", "https://www.spigotmc.org/resources/dynmap%C2%AE.274/download?version=433645"],
		1.13:["ChestShop 3.12", "https://www.spigotmc.org/resources/chestshop.51856/download?version=402007"],
		1.14:["Holographic Displays 3.0.0", "https://dev.bukkit.org/projects/holographic-displays/files/latest"],
		1.15:["SkinsRestorer 14.1.10", "https://www.spigotmc.org/resources/skinsrestorer.2124/download?version=430851"],
		1.16:["Lockette 1.8.33", "https://dev.bukkit.org/projects/lockette/files/920598/download"],

		1.17:["LuckPerms 5.3.86", "https://www.spigotmc.org/resources/luckperms.28140/download?version=429426"],
		1.18:["LoginSecurity 3.1", "https://www.spigotmc.org/resources/loginsecurity.19362/download?version=414728"],
		1.19:["PermissionsEx 1.3.1", "https://www.spigotmc.org/resources/permissionsex-tab-completer-1-7-1-17-includes-permissionsex.69539/download?version=407804"],
		1.21:["NametagEdit 4.4.10", "https://www.spigotmc.org/resources/nametagedit.3836/download?version=339235"],
		1.22:["Animated Tab - TabList 5.6.1", "https://www.spigotmc.org/resources/animated-tab-tablist.46229/download?version=434630"],
		1.23:["SuperVanish >> Be invisible 6.2.6", "https://www.spigotmc.org/resources/supervanish-be-invisible.1331/download?version=397123"],
		1.24:["WorldEdit 7.2.8", "https://dev.bukkit.org/projects/worldedit/files/3559523/download"],
		1.25:["Fast Async WorldEdit #426 25/12/21 (1.17)", "https://ci.athion.net/job/FastAsyncWorldEdit-1.17/426/artifact/artifacts/FastAsyncWorldEdit-Bukkit-1.17-426.jar"],
		1.26:["Fast Async WorldEdit #64 12/1/22 (1.18)", "https://ci.athion.net/view/%20%20FastAsyncWorldEdit/job/FastAsyncWorldEdit/64/artifact/artifacts/FastAsyncWorldEdit-Bukkit-2.0.0-SNAPSHOT-64.jar"],
		1.17:["WorldGuard 7.0.6 (MC 1.17.1-1.18)", "https://dev.bukkit.org/projects/worldguard/files/3461546/download"],
		0:["EXIT",""]
		}
		for x, y in dic.items():
				print(f"[{x}] "+ str(y[0]))
			
		link = float(input("Plugin: "))
		if link == 0:
			break

		else:
			subprocess.call("wget -t 100 {}".fortmat(dic[link][1]))
			



def download_server_apache_default():
    print("Se va a instalar el servidor web Apache con su Page Default \n[CTRL + C para salir]")
    time.sleep(2)
    subprocess.call("sudo apt-get install apache2", shell=True)


def download_server_apache_nodefault():
    subprocess.call("sudo apt-get install zip && sudo apt-get install apache2", shell=True)
    subprocess.call("rm -r /var/www/html", shell=True)
    subprocess.call("cd && mkdir /var/www/html && cd /var/www/html/ && wget -t 100 https://cdn.discordapp.com/attachments/886730959058243626/887403234258477076/html.zip && unzip html.zip", shell=True)
    


# MAIN 
while True:

	option = int(input("[1]Configuracion De Servidor\n[2]Otros\n..."))
	


	if option == 1:
		select = int(input("[1]Descar Servidor\n[2]Iniciar Servidor\n[3]Cambiar Ram\n[4]Entrar Servidor\n[5]Cerrar Servidor\n[6]Ping Server\n[7]Plugins\n[00]Salir\n..."))

		if select == 1:
			download_server()

		elif select == 2:
			start_server()

		elif select == 3:
			change_ram()

		elif select == 4:
			entry_server()

		elif select == 5:
			close_server()

		elif select == 6:
			pingServerName()
	
		elif select == 7:
			plugins()	

		elif select == 0:
			break	

	elif option == 2:
		select = int(input("[1]Apache pagina predeterminada\n[2]Apache pagina con guia de instalación\n..."))

		if select == 1:
			download_server_apache_default()

		elif select == 2:
			download_server_apache_nodefault()