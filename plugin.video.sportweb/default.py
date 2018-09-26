# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Linker de las webs ArenaVision, DinoZap, VerPlusOnline Deportes y Verliga.Net Bad-Max
# Version 0.0.1 (20.01.2018)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a la librería plugintools de Jesús (www.mimediacenter.info)

import os
import sys
import urllib
import urllib2
import re

import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
import time

import plugintools, requests
import resolvers
from __main__ import *
import datetime, locale
from datetime import datetime, timedelta

addonName           = xbmcaddon.Addon().getAddonInfo("name")
addonVersion        = xbmcaddon.Addon().getAddonInfo("version")
addonId             = xbmcaddon.Addon().getAddonInfo("id")
addonPath           = xbmcaddon.Addon().getAddonInfo("path")

version = "(v0.0.7)"

mi_data = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/plugin.video.sportweb/'))
playlists = mi_data
temp = mi_data

if not os.path.exists(mi_data):
	os.makedirs(mi_data)  # Si no existe el directorio, lo creo

live365 = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.sport365.live/'))
carta365 = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.deportesalacarta/'))
logo365 = "https://i.imgur.com/qgc9X1E.png"
fondo365 = "https://i.imgur.com/Bffhqbl.png"

parser = "        [COLOR blue][B]SportsWeb v0.0.2      [COLOR red]····[COLOR yellow]by Bad-Max[COLOR red]····[/B][/COLOR]"
logo="https://i.imgur.com/aBFk6WM.png"
fondo = "https://i.imgur.com/3Wi05Fv.png"

######################################### ArenaVision ###################################################################3
#url = 'http://www.arenavision.in'
#url = "http://www.arenavision.ru/guide"
#url_ref_arena = 'http://www.arenavision.in/'
#url_agenda_arena = 'http://arenavision.in/agenda'
#url_agenda_arena = 'http://www.arenavision.in/schedule'
#url_agenda_arena = 'http://www.arenavision.top/iguide'
url_ref_arena = 'http://www.arenavision.top/'
url_agenda_arena = 'http://www.arenavision.top/guide'
dicdias={'Monday':'Lunes','Tuesday':'Martes','Wednesday':'Miercoles','Thursday':'Jueves','Friday':'Viernes','Saturday':'Sabado','Sunday':'Domingo'}
version_arena = "(v0.4)"
fich_hora = xbmc.translatePath(os.path.join('special://userdata/addon_data/plugin.video.sportweb/horario_arenavision.txt'))

######################################### AceListing ###################################################################3
url_acelist = 'https://acelisting.in/'
logo_acelist = "https://i.imgur.com/tOcOo9K.png"
fondo_acelist = "https://i.imgur.com/USXpk0u.png"


######################################### VipRacing ###################################################################3
url_vip = 'http://vipracing.tv/'
logo_vip = "https://i.imgur.com/F69Zcto.png"
fondo_vip = "https://i.imgur.com/M5k5w9Y.png"


######################################### DinoZap ###################################################################3
url_dino = 'http://dinozap.info'
url_ref_dino = 'http://dinozap.info/'
url_agenda_dino = 'http://www.dinozap.tv/prog.txt'
logo_dino = "http://i.imgur.com/64kVOaM.png"
fondo_dino = "http://i.imgur.com/DGTkJqB.png"


######################################### VerLiga.net ###################################################################3
url_verliga = 'http://www.verliga.net'
url_ref_verliga = 'http://www.vergol.com/'
version_verliga = "(v0.0.2)"
logo_verliga = 'http://i.imgur.com/P89RUX4.png'
fondo_verliga = 'http://i.imgur.com/4pKVRDk.png'
logo_zap = "http://images.digopaul.com/wp-content/uploads/related_images/2015/09/09/zapping_1.jpg"

######################################### VerPlusOnline Deportes ###################################################################
url_plus = 'http://verplusonline.com/programacion-deportiva/'
url_ref_plus = 'http://verplusonline.com/'
logo_plus = "https://i.imgur.com/bLEaCPV.png"
fondo_plus = "http://i.imgur.com/DGTkJqB.png"

######################################### VerTelevisor.com Deportes ################################################################
url_tele = 'http://www.vertelevisor.com/category/deportes/'
url_ref_tele = 'http://www.vertelevisor.com/'
logo_tele = "https://i.imgur.com/TyTVGam.png"
fondo_tele = "http://i.imgur.com/DGTkJqB.png"





# Entry point
def run():
	plugintools.log('[%s %s] Running %s... ' % (addonName, addonVersion, addonName))

	# Obteniendo parámetros...
	params = plugintools.get_params()
    
	
	if params.get("action") is None:
		main_list(params)
	else:
		action = params.get("action")
		exec action+"(params)"
	

	#main_list(params)

	plugintools.close_item_list()            



# Main menu
def main_list(params):
	thumbnail="http://i.imgur.com/Ehe3ZkR.png"
	fanart="http://i.imgur.com/tD4QHCf.png"
	datamovie={}
	
	plugintools.add_item(action="",url="",title="[COLOR blue][B]                 Sports-Web[/B]   [I]"+version+"[/I][/COLOR][COLOR yellow][I]    **** byBad-Max ****[/I][/COLOR]",thumbnail=logo,fanart=fondo,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=logo,  fanart=fondo, folder=False, isPlayable=False)

	plugintools.add_item(action="arena_dmax0",url="",title="[COLOR red][B]-ArenaVision  [COLOR blue](Acestream)[/B][/COLOR]",thumbnail="https://elrincondesereblog.files.wordpress.com/2015/12/2.png?w=768",fanart="http://1.bp.blogspot.com/-MY6Pz_Ucljk/Ut1FZLWUAcI/AAAAAAAAARo/bG-RAvuPKAM/s1600/futbol_dic2013_phixr.jpg",folder=True,isPlayable=False)
	plugintools.add_item(action="acelisting0",url="",title="[COLOR aqua][B]-Acelisting.in  [COLOR blue](Acestream)[/B][/COLOR]",thumbnail=logo_acelist,fanart=fondo_acelist,folder=True,isPlayable=False)

	if os.path.exists(live365):  ## Si tiene el addon plugin.video.sport365.live lo uso como 1ª opción, si no, si tienen DeportesalaCarta uso ese sport365... y si no tiene ninguno de los 2, no aparecerá en el menú ninguna opción
		plugintools.add_item(action="runPlugin",url="plugin://plugin.video.sport365.live/?ex_link&foldername=Sport365%20LIVE&mode=site2&params=%7b%27_service%27%3a%20%27sport365%27%2c%20%27_act%27%3a%20%27ListChannels%27%7d",title="[COLOR orange][B]-Sport365 (De Addon sport365.live)[/B][/COLOR]",thumbnail=logo365,fanart=fondo365,folder=True,isPlayable=False)
	elif os.path.exists(carta365):
		plugintools.add_item(action="runPlugin",url="plugin://plugin.video.deportesalacarta/?ewogICAgImFjdGlvbiI6ICJtYWlubGlzdCIsIAogICAgImNhdGVnb3J5IjogImRlcG9ydCIsIAogICAgImNoYW5uZWwiOiAic3BvcnQzNjUiLCAKICAgICJmYW5hcnQiOiAiIiwgCiAgICAiaW5mb0xhYmVscyI6IHt9LCAKICAgICJsYW5ndWFnZSI6ICJlcyIsIAogICAgInRodW1ibmFpbCI6ICJodHRwOi8vaS5pbWd1ci5jb20vaEoydmhpcC5wbmciLCAKICAgICJ0aXRsZSI6ICJTcG9ydDM2NSIsIAogICAgInRvdGFsSXRlbXMiOiAwLCAKICAgICJ2aWV3bW9kZSI6ICJsaXN0Igp9",title="[COLOR orange][B]-Sport365 (De Addon DeportesalaCarta)[/B][/COLOR]",thumbnail=logo365,fanart=fondo365,folder=True,isPlayable=False)
	
	plugintools.add_item(action="vipracing0",url="",title="[COLOR peru][B]-VipRacing[/B][/COLOR]",thumbnail=logo_vip,fanart=fondo_vip,folder=True,isPlayable=False)
	plugintools.add_item(action="verliganet0",url="",title="[COLOR green][B]-VerLiga.net[/B][/COLOR]",thumbnail='http://i.imgur.com/P89RUX4.png',fanart='http://i.imgur.com/4pKVRDk.png',folder=True,isPlayable=False)
	plugintools.add_item(action="vertelevisor0",url="",title="[COLOR gold][B]-VerTelevisor.com Deportes[/B][/COLOR]",thumbnail=logo_tele,fanart=fondo_tele,folder=True,isPlayable=False)
	plugintools.add_item(action="verplus0",url="",title="[COLOR lime][B]-VerPlusOnline Deportes[/B][/COLOR]",thumbnail=logo_plus,fanart=fondo_plus,folder=True,isPlayable=False)
	plugintools.add_item(action="dinozapmax0",url="",title="[COLOR blue][B]-DinoZap [COLOR red](Web OFF por ahora)[/B][/COLOR]",thumbnail="http://i.imgur.com/F4VGZUJ.png",fanart=fondo_dino,folder=True,isPlayable=False)


	
def runPlugin(params):
	url = params.get("url")

	builtin = 'RunPlugin(%s)' %url
	xbmc.executebuiltin(builtin)   


		
		
		


#########################ARENAVISION#########################################
def arena_dmax0(params):
	plugintools.log("[%s %s] http://arenavision.in/agenda %s " % (addonName, addonVersion, repr(params)))
	fanart = "http://iforo.3djuegos.com/files_foros/39/395w.png"
	
	plataforma = arena_plataforma()

	headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0', "Referer": url_agenda_arena, "cookie": "beget=begetok"}
	
	r=requests.get(url_agenda_arena, headers=headers)
	data = r.content
	data = data.replace("]" , "CORCHETE")
	
	plugintools.add_item(action="",url="",title="[COLOR blue][B]                 ArenaVision[/B]   [I]"+version_arena+"[/I][/COLOR][COLOR yellow][I]    **** byBad-Max ****[/I][/COLOR]",thumbnail="http://s15.postimg.org/bicwnygez/ARENAVISION.jpg",fanart=fanart,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail="http://static.wixstatic.com/media/41d000_0ba0b768e7c98113d7fb91b13075748d.png_srz_980_236_85_22_0.50_1.20_0.00_png_srz", fanart=fanart, folder=False, isPlayable=False)

	plugintools.add_item(action="cambia_hora_arena",url="",title="[COLOR yellow][B]- Cambiar Diferencia Horaria -[/COLOR][/B]",thumbnail="http://image.slidesharecdn.com/1esopresentaciontema1-110109052848-phpapp02/95/tema-1-la-tierra-1-eso-28-728.jpg?cb=1294550960",fanart=fanart,folder=True,isPlayable=False)

	plugintools.add_item(action="arenazaping",url="",title="[COLOR orange][B]- Zapping de Canales -[/COLOR][/B]",thumbnail="http://lafava.com/wp-content/uploads/2015/06/zapping1.jpg",fanart="http://deportes.uprm.edu/wp-content/uploads/2014/11/Foto-Collage-Resena-principal.png",folder=True,isPlayable=False)

	plugintools.add_item(action="",url="",title="",thumbnail="http://static.wixstatic.com/media/41d000_0ba0b768e7c98113d7fb91b13075748d.png_srz_980_236_85_22_0.50_1.20_0.00_png_srz", fanart=fanart, folder=False, isPlayable=False)

	lineas = plugintools.find_multiple_matches(data,'<tr><td(.*?)CORCHETE</td>')

	#***********  Control de Diferencias Horarias Bad-Max 15-10-16  *******************
	if not os.path.exists(fich_hora):
		diferencia = "00:00"
		file_hora=open(fich_hora, "w+")
		file_hora.write("00:00")
		file_hora.close()
	else:
		file_hora=open(fich_hora, "r")
		diferencia = file_hora.read()
		file_hora.close()
	#***********  Control de Diferencias Horarias Bad-Max 15-10-16  *******************

	diferencia = diferencia + ":00"
		
	i=0
	fecha = "01/01/2001"
	while i < len(lineas):
		linea = "COMIENZO" + lineas[i] + "]</td>".replace(" CET","").replace(" CEST","")
		linea = linea.replace(' style="height: 17px;"' , "")  # 25-11-17 hay solo algunas líneas donde incluyen ese texto... así q lo quito
		apartados = plugintools.find_multiple_matches(linea,'auto-style13">(.*?)</td')

		lin_item = ""
		cuenta = 0
		cuenta2 = 0
		canales = ""
		canales0=""
		es_fecha = False

		for item in apartados:
			item = 'auto-style13">' +  item + "</td>"
			item = item.replace(" CET</td>","</td>").replace(" CEST</td>","</td>").strip()
			plugintools.log("**************************Items Apartado: "+item+"*****************************")

			texto = plugintools.find_single_match(item,'auto-style13">(.*?)</td')  ## .replace("SOCCER","Fútbol").replace("<br />"," / ")
			texto = texto.replace("CORCHETE","]").replace("SOCCER","Fútbol").replace("<br />","").replace("FOOTBALL","Rugby Americano").replace("PRESEASON","Pretemporada").replace("OLYMPICS","Olimpicos").replace("BASKETBALL","Baloncesto").replace("SWIMMING","Natación")  # .decode('unicode_escape').encode('utf8')
			plugintools.log("**************************Items TEXTO: "+texto+"*****************************")
			cuenta = cuenta + 1
			
			texto_fec = plugintools.find_single_match(linea,'px">(.*?)</td')  ## 06-04-18.... han vuelto a cambiar el formato para la fecha
			if len(texto_fec) > 0:  # Fecha ... 11/08/16... casi siempre, pero cuando les sale de los huevos, ponen el 1º los canales y la fecha el último
				#voy a buscar la fecha y los canales xq van cambiando.
				texto2 = texto_fec  ## 06-04-18
				for item2 in apartados:
					texto2 = texto2.replace("<br />","").replace("FOOTBALL","Rugby Americano").replace("PRESEASON","Pretemporada").replace("OLYMPICS","Olimpicos").replace("BASKETBALL","Baloncesto").replace("SWIMMING","Natación")  # .decode('unicode_escape').encode('utf8')
					barra1 = texto2[2:3]
					barra2 = texto2[5:6]
					if barra1 == "/" and barra2 == "/":
						if fecha <> texto2:
							fecha = texto2
							# Voy a sacar el día de la semana
							# Pero primero voy a corregir que muchas veces ponen el mes y/o el año mal
							fecha_actu=time.strftime("%d/%m/%Y", time.localtime())
							dia_actu = fecha_actu[:2]
							mes_actu = fecha_actu[3:5]
							ano_actu = fecha_actu[6:]
							mes_capullos = fecha[3:5]
							ano_capullos = fecha[6:]
							if mes_actu <> mes_capullos and dia_actu <> "01":
								if mes_actu == "02" and dia_actu <= "27":
									fecha=fecha.replace("/"+mes_capullos+"/", "/"+mes_actu+"/")
								else:
									if mes_actu <> "02" and dia_actu < "30":
										fecha=fecha.replace("/"+mes_capullos+"/", "/"+mes_actu+"/")
							if ano_actu <> ano_capullos and dia_actu+mes_actu <> "31/12" and dia_actu+mes_actu <> "01/01":
								fecha=fecha.replace("/"+ano_capullos, "/"+ano_actu)

							t0=time.strptime(fecha, '%d/%m/%Y')
							
							dia_ing=time.strftime("%A",t0)
							dia_esp = dicdias[dia_ing]

							#Creo una línea
							line_fech = "[COLOR lleyow][B][I]" + dia_esp + ", " + fecha + "[/COLOR][/B][/I]"
							plugintools.add_item(action="",url="",title=line_fech,thumbnail="http://static.wixstatic.com/media/41d000_0ba0b768e7c98113d7fb91b13075748d.png_srz_980_236_85_22_0.50_1.20_0.00_png_srz", fanart=fanart, folder=False, isPlayable=False)
							
					idioma = plugintools.find_single_match(texto,'[(.*?)]')
					if len(idioma) <> 0:  # son los canales... a ver si es verdad :-)
						canales0=texto

			if cuenta  == 1:  # Hora
				#***********  Control de Diferencias Horarias Bad-Max 15-10-16  *******************
				hora_esp = texto.replace(" CET","").replace(" CEST","").strip()
				hora_esp = hora_esp.replace("." , ":").replace("Â ","")
				hora_esp = hora_esp + ":00"  # Añado los segundos
				hora_dif = diferencia + ":00"  # Añado los segundos
				lista_esp = hora_esp.split(":")
				lista_dif = diferencia.replace("-","").split(":")

				#plugintools.log("**************************HoraEsp "+hora_esp)
				try:
					esp_hora=int(lista_esp[0])
					esp_minuto=int(lista_esp[1])
					esp_segundo=int(lista_esp[2])

					dif_hora=int(lista_dif[0])
					dif_minuto=int(lista_dif[1])
					dif_segundo=int(lista_dif[2])
					
					h1 = datetime(2012, 12, 12, esp_hora, esp_minuto, 0)
					
						
					dh = timedelta(hours=dif_hora) 
					dm = timedelta(minutes=dif_minuto)          
					ds = timedelta(seconds=dif_segundo)
					
					
					if "-" in diferencia:  # Hay que restar horas
						resultado1 =h1 - ds
						resultado2 = resultado1 - dm
						resultado = resultado2 - dh
					else:  # Hay que sumar Horas
						resultado1 =h1 + ds
						resultado2 = resultado1 + dm
						resultado = resultado2 + dh

					
					hora="[COLOR lightblue]" + resultado.strftime("%H:%M:%S") + "h[/COLOR]"
					hora = hora.replace(":00h","h")
					#***********  Control de Diferencias Horarias Bad-Max 15-10-16  *******************
				except:
					hora="[COLOR lightblue]Mal Definida[/COLOR]"
					
				lin_item = lin_item + "[COLOR red]["+hora+"]   "
				
				

			elif cuenta == 2:  # Deporte
				lin_item = lin_item + "[COLOR orange]("+texto

			elif cuenta == 3:  # Evento
				lin_item = lin_item + "-"+texto.title()+")    "

			elif cuenta == 4:  # Partido
				lin_item = lin_item + "[COLOR green]"+texto.title()+"[/COLOR]"
				

			elif cuenta == 5:  # or len(canales0) > 0:  # Canales
				if len(canales0) > 0:  # Ya lo han puesto donde les da la gana
					canales = canales0.replace("CORCHETE","]")
				else:	
					canales = texto
				lin_item  = lin_item + "[COLOR red] Canales: "	+ canales + "[/COLOR]"
					
		plugintools.add_item(action="arenazaping",url=canales,title=lin_item,thumbnail="http://s15.postimg.org/bicwnygez/ARENAVISION.jpg", fanart=fanart, folder=True, isPlayable=False)
		i = i + 1
			
def cambia_hora_arena(params):

	if not os.path.exists(fich_hora):
		diferencia = "00:00"
		file_hora=open(fich_hora, "w+")
		file_hora.write("00:00")
		file_hora.close()
	else:
		file_hora=open(fich_hora, "r")
		diferencia = file_hora.read()
		file_hora.close()

	pide = plugintools.keyboard_input(diferencia, 'Introduzca Diferencia (con [COLOR red]Signo Menos[/COLOR] si son a Disminuir) [COLOR green]XX:XX[/COLOR]')
	
	if pide <> diferencia:
		file_hora=open(fich_hora, "w+")
		file_hora.write(pide)
		file_hora.close()
		xbmcgui.Dialog().ok( "- Tenga en Cuenta -" , "Para que el cambio tenga efecto en la Guía, tendrá que salir del Parser y volver a entrar." )

	return

	
		
def arena_pon_canales(params):
	canales = params.get("url")
	title = params.get("title")

	plugintools.add_item(action="",url="",title="[COLOR blue][B]                 ArenaVision[/B]   [I]"+version+"[/I][/COLOR][COLOR yellow][I]    **** byBad-Max ****[/I][/COLOR]",thumbnail=thumbnail,fanart=fanart,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=thumbnail, fanart=fanart, folder=False, isPlayable=False)

	plugintools.add_item(action="",url="",title=title,thumbnail=thumbnail, fanart=fanart, folder=False, isPlayable=False)

	canales = ">" + canales.replace("]", "];#>").replace("/","")
	canales_Idioma = plugintools.find_multiple_matches(canales,'>(.*?)#')
	
	for item in canales_Idioma:
		cada_canal = item.split("-")
		
		#En el último quedará el canal y el idioma: "25 [Spa]"
		idioma0 = cada_canal[-1]
		idioma0 = idioma0.replace("[",">").replace("]","<")
		idioma = " [" + plugintools.find_single_match(idioma0,'>(.*?)<') + "]"
		
		for item2 in cada_canal:
			item2 = item2.strip()
			if "[" in item2:  # El último
				if item2[:1] == "S":  # Es SopCast
					linea = "[COLOR orange]Ver en Canal:   [COLOR lightgreen][B]"+item2+"        [/B][COLOR blue][I](SopCast)[/COLOR][/I]"
				else:
					linea = "[COLOR orange]Ver en Canal:   [COLOR lightgreen][B]"+item2+"        [/B][COLOR red][I](Acestream)[/COLOR][/I]"
				canal0 = item2.replace("[","<")
				canal = plugintools.find_single_match(canal0,'(.*?)<')
			else:
				if "S" in item2:  # Es SopCast
					linea = "[COLOR orange]Ver en Canal:   [COLOR lightgreen][B]"+item2+idioma+"        [/B][COLOR blue][I](SopCast)[/COLOR][/I]"
				else:
					linea = "[COLOR orange]Ver en Canal:   [COLOR lightgreen][B]"+item2+idioma+"        [/B][COLOR red][I](Acestream)[/COLOR][/I]"
				canal = item2
			
			laurl = busca_aces(canal)
			if len(laurl) > 0:
				url_montada = laurl + "&name=" + title
				#plugintools.log("********************URL: "+url_montada+"***********************")	
				plugintools.add_item(action="runPlugin",url=url_montada,title=linea.replace(";","").replace("CORCHETE","]"),thumbnail=thumbnail,fanart=fanart,folder=False,isPlayable=True)
			

def busca_aces(canal):

	el_canal = int(canal) - 1
	#Pngo -1 pues el array "todos" en python, empieza la 1ª posición en CERO, no en UNO
	
	url = todos[el_canal]
	'''
	#Ya al comienzo, si no es kodi 17, en el array pone toda la url_montada
	if kodi16:
		return url
	'''

	headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0', "Referer": url, "cookie": "beget=begetok"}
	r=requests.get(url, headers=headers)
	data = r.content
	
	linkace = plugintools.find_single_match(data,'href="acestream(.*?)"')
	
	if ".acelive" in data:
		data2=data.replace('"' , 'COMILLAS')
		linkace = plugintools.find_single_match(data2,'auto-style1COMILLAS><a href=COMILLAS(.*?)COMILLAS').replace('"' , '')
		url_montada = "plugin://program.plexus/?url=" + linkace + "&mode=1"
	
	else:
		url_montada = "plugin://program.plexus/?url=acestream" + linkace + "&mode=1"
		
	return url_montada



			
def arenazaping(params):
	fanart = params.get("fanart")
	thumbnail = params.get("thumbnail")

	plugintools.add_item(action="",url="",title="[COLOR blue][B]   Canales   ArenaVision[/B]   [I]"+version+"[/I][/COLOR][COLOR yellow][I]    **** byBad-Max ****[/I][/COLOR]",thumbnail=thumbnail,fanart=fanart,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=thumbnail, fanart=fanart, folder=False, isPlayable=False)

	headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0', "Referer": url_agenda_arena, "cookie": "beget=begetok"}
	r0=requests.get(url_agenda_arena, headers=headers)
	data0 = r0.content

	
	grupo = plugintools.find_single_match(data0,'id="navigation(.*?)FAQ</a')  ## 07-04-18
	plugintools.log("********************GRUPO: "+grupo+"***********************")	
	canales = plugintools.find_multiple_matches(grupo,'a href=(.*?)/li>')
	
	for item in canales:
		item = item.replace('"http' , 'COMIENZOhttp').replace('" title' , 'FIN title')
		if "http://arena" in item:
			canalaces = plugintools.find_single_match(item,'COMIENZO(.*?)FIN')
			titulo = plugintools.find_single_match(item,'title="">(.*?)<')

			plugintools.add_item(action="lanza_aces",url=canalaces,title="[COLOR red][B]"+titulo+"[/COLOR][/B]",thumbnail=thumbnail,fanart=fanart,folder=True,isPlayable=False)
			
	
	
def lanza_aces(params):
	fanart = params.get("fanart")
	thumbnail = params.get("thumbnail")
	url = params.get("url")
	titulo = params.get("title")

	
	headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0', "Referer": url, "cookie": "beget=begetok"}
	r1=requests.get(url, headers=headers)
	data1 = r1.content

	ace = "acestream:" + plugintools.find_single_match(data1,'"acestream:(.*?)"')
	
	url_montada = "plugin://program.plexus/?url=acestream%3A%2F%2F" + ace + "&mode=1&name=ID+de+Usuario+%28+acestream%3A%2F%2F63d893d4db0f0c591436c7a88b6f6fc27e84a5b8%29&iconimage=C%3A%5CUsers%5Cusuario%5CAppData%5CRoaming%5CKodi%5Caddons%5Cprogram.plexus%5Cresources%5Cart%5Cacestream-menu-item.png"
	plugintools.add_item(action="runPlugin",url=url_montada,title="Lanzar el Canal "+titulo,thumbnail=thumbnail,fanart=fanart,folder=False,isPlayable=True)
	


def arena_sop(params):
	fanart = params.get("fanart")
	thumbnail = params.get("thumbnail")
	title = "          ·····  " + params.get("title").replace("-","") + "  ·····"

	plugintools.add_item(action="",url="",title="[COLOR blue][B]                 ArenaVision[/B]   [I]"+version+"[/I][/COLOR][COLOR yellow][I]    **** byBad-Max ****[/I][/COLOR]",thumbnail=thumbnail,fanart=fanart,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=thumbnail, fanart=fanart, folder=False, isPlayable=False)

	plugintools.add_item(action="",url="",title=title,thumbnail=thumbnail, fanart=fanart, folder=False, isPlayable=False)

	r = requests.get(url)	
	data = r.content
	
	canales = plugintools.find_single_match(data,'active"/sopcast(.*?)</ul></li>')
	cada_canal = plugintools.find_multiple_matches(canales,'href=(.*?)/a>')
	
	i = 0
	while i < len(cada_canal):
		item = cada_canal[i]
		#for item in cada_canal:
		canal = url + plugintools.find_single_match(item,'"(.*?)"')
		titulo = "-Ver ArenaVisión " + plugintools.find_single_match(item,">ArenaVision(.*?)<")

		plugintools.log("************Canal: "+canal+"**************")
		plugintools.log("************Titulo: "+titulo+"**************")

		url_montada = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='+canal+'%26referer='+url_ref_arena
		plugintools.add_item(action="runPlugin",url=url_montada,title=titulo,thumbnail=thumbnail,fanart=fanart,folder=False,isPlayable=True)
		
		i = i + 1




def arena_plataforma():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'	

		
		
		


##############################################################################		
######################### AceListing #########################################
##############################################################################		
def acelisting0(params):

	headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0', "Referer": url_acelist}
	
	r=requests.get(url_acelist, headers=headers)
	data = r.content
	
	plugintools.add_item(action="",url="",title="[COLOR blue][B]                 AceListing.in[/B]   [I]v0.0.1[/I][/COLOR][COLOR yellow][I]    **** byBad-Max ****[/I][/COLOR]",thumbnail=logo_acelist,fanart=fondo_acelist,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=logo_acelist, fanart=fondo_acelist, folder=False, isPlayable=False)

	plugintools.add_item(action="cambia_hora_arena",url="",title="[COLOR yellow][B]- Cambiar Diferencia Horaria -[/COLOR][/B]",thumbnail="http://image.slidesharecdn.com/1esopresentaciontema1-110109052848-phpapp02/95/tema-1-la-tierra-1-eso-28-728.jpg?cb=1294550960",fanart=fondo_acelist,folder=True,isPlayable=False)


	#***********  Control de Diferencias Horarias Bad-Max 15-10-16  *******************
	if not os.path.exists(fich_hora):
		diferencia = "00:00"
		file_hora=open(fich_hora, "w+")
		file_hora.write("00:00")
		file_hora.close()
	else:
		file_hora=open(fich_hora, "r")
		diferencia = file_hora.read()
		file_hora.close()
	#***********  Control de Diferencias Horarias Bad-Max 15-10-16  *******************

	diferencia = diferencia + ":00"


	dias = plugintools.find_multiple_matches(data,'colspan="3(.*?)class="success')
	#plugintools.log("**************************DATA: "+data + "********************************")
	
	fecha = "01/01/2001"
	for item in dias:
		item = item.replace('Channel ' , 'Channel>').replace("Language " , "Language>").replace("title = " , "title>").replace("\n" , "")
		# Cojo primero la fecha del día
		texto_fec = plugintools.find_single_match(item,'h4>(.*?)</h4')
		texto_fec = texto_fec.strip().title()

		#Cambiamos los meses a Español
		texto_fec = texto_fec.replace("January","Enero").replace("February","Febrero").replace("March","Marzo").replace("April","Abril").replace("May","Mayo").replace("June","Junio").replace("July","Julio").replace("August","Agosto").replace("September","Septiembre").replace("October","Octubre").replace("November","Noviembre").replace("December","Diciembre")

		#Cambiamos los dias de la semana a Español
		texto_fec = texto_fec.replace("Monday","Lunes,").replace("Tuesday","Martes,").replace("Wednesday","Miércoles,").replace("Thursday","Jueves,").replace("Friday","Viernes,").replace("Saturday","Sábado,").replace("Sunday","Domingo,")

		plugintools.add_item(action="",url="",title="[COLOR white][B]"+texto_fec+"[/B][/COLOR]",thumbnail=logo_acelist, fanart=fondo_acelist, folder=False, isPlayable=False)

		# Separo los diferentes eventos del día
		eventos = plugintools.find_multiple_matches(item,'tr>(.*?)</div')

		for item2 in eventos:
			lin_item = ""
			# Busco la hora
			#***********  Control de Diferencias Horarias Bad-Max 15-10-16  *******************
			horaesp = plugintools.find_single_match(item2,'text-right">(.*?)</td') + "</td"
			hora_esp = plugintools.find_single_match(horaesp,'text-right">(.*?)</td').strip()
			
			hora_esp = hora_esp + ":00"  # Añado los segundos
			hora_dif = diferencia
			lista_esp = hora_esp.split(":")
			lista_dif = diferencia.replace("-","").split(":")

			try:
				esp_hora=int(lista_esp[0]) + 2  ## Le sumo 2h para q me saque la hora española
				if esp_hora == 24:
					esp_hora = 0
				elif esp_hora == 25:
					esp_hora = 1
				esp_minuto=int(lista_esp[1])
				esp_segundo=int(lista_esp[2])

				dif_hora=int(lista_dif[0])
				dif_minuto=int(lista_dif[1])
				dif_segundo=int(lista_dif[2])
				
				h1 = datetime(2012, 12, 12, esp_hora, esp_minuto, 0)
				
					
				dh = timedelta(hours=dif_hora) 
				dm = timedelta(minutes=dif_minuto)          
				ds = timedelta(seconds=dif_segundo)
				
				
				if "-" in diferencia:  # Hay que restar horas
					resultado1 =h1 - ds
					resultado2 = resultado1 - dm
					resultado = resultado2 - dh
				else:  # Hay que sumar Horas
					resultado1 =h1 + ds
					resultado2 = resultado1 + dm
					resultado = resultado2 + dh

				
				hora="[COLOR lightblue]" + resultado.strftime("%H:%M:%S") + "h[/COLOR]"
				hora = hora.replace(":00h","h")
				#***********  Control de Diferencias Horarias Bad-Max 15-10-16  *******************
			except:
				hora="[COLOR lightblue]Mal Definida[/COLOR]"

			lin_item = lin_item + "[COLOR red]["+hora+"]   "
					
			# Vamos a por el tipo de Deporte
			deporte = plugintools.find_single_match(item2,'<td>(.*?)</td').strip()
			deporte = deporte.replace("SOCCER","Fútbol").replace("TENNIS","Tenis").replace("FOOTBALL","Rugby Americano").replace("PRESEASON","Pretemporada").replace("OLYMPICS","Olimpicos").replace("BASKETBALL","Baloncesto").replace("SWIMMING","Natación")  # .decode('unicode_escape').encode('utf8')
			compe = plugintools.find_single_match(item2,'alt="(.*?)"').strip()
			competi = "-" + plugintools.find_single_match(compe,'>(.*?)<br').strip().title()
			lin_item = lin_item + "[COLOR orange]("+deporte+competi+")  "
			
			# Vamos a por el Encuentro
			encuentro = plugintools.find_single_match(item2,'title>"(.*?)<br').title().strip()
			lin_item = lin_item + "[COLOR lime][B]"+encuentro+"[/B]  "
			
			# Vamos a por los Canales
			canales = plugintools.find_multiple_matches(item2,'"tooltip(.*?)</a')
			loscanales = "[COLOR red]Canales: "
			aces = ">"
			primeravez = True
			for item3 in canales:
				lalinea = "canal>" + plugintools.find_single_match(item3,'Channel>(.*?)">') + "<"
				elcanal =  plugintools.find_single_match(lalinea,'canal>(.*?)<br')
				idioma =  "[" + plugintools.find_single_match(lalinea,'Language>(.*?)"') + "]"
				link = plugintools.find_single_match(item3,'href="(.*?)"')
				if primeravez:
					loscanales = loscanales + elcanal + idioma
					aces = aces + link
					primeravez = False
				else:
					loscanales = loscanales +" , " + elcanal + idioma
					aces = aces + "<>" +link
					
			lin_item = lin_item + loscanales + "[/COLOR]"	
			aces = aces + "<"

			plugintools.add_item(action="lanza_acelist",url="",title=lin_item,extra=aces,page=loscanales,thumbnail=logo_acelist, fanart=fondo_acelist, folder=True, isPlayable=False)

		
		
		
def lanza_acelist(params):
	lacabecera = params.get("title")	
	loscanales = params.get("page")	
	links = params.get("extra")	

	canales = ">" + loscanales.replace(" , ","<>") + "<"
	cabecera =  plugintools.find_single_match(lacabecera,'(.*?)Canales').strip() + "[/COLOR]"
	
	plugintools.add_item(action="",url="",title=cabecera,thumbnail=logo_acelist,fanart=fondo_acelist,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=logo_acelist, fanart=fondo_acelist, folder=False, isPlayable=False)

	canal = plugintools.find_multiple_matches(canales,'>(.*?)<')
	link = plugintools.find_multiple_matches(links,'>(.*?)<')
	
	i = 0
	for item in canal:
		item = item.replace("Canales: " , "")
		titu = "[COLOR red]-Ver en Canal " + item + "[/COLOR]"
		ace = link[i]
		
		url_montada = "plugin://program.plexus/?url=acestream%3A%2F%2F" + ace + "&mode=1&name=ID+de+Usuario+%28+acestream%3A%2F%2F63d893d4db0f0c591436c7a88b6f6fc27e84a5b8%29&iconimage=C%3A%5CUsers%5Cusuario%5CAppData%5CRoaming%5CKodi%5Caddons%5Cprogram.plexus%5Cresources%5Cart%5Cacestream-menu-item.png"
		plugintools.add_item(action="runPlugin",url=url_montada,title=titu,thumbnail=logo_acelist, fanart=fondo_acelist,folder=False,isPlayable=True)
		i = i + 1
	
	
	


	
#########################################################################		
######################### VipRacing #####################################
#########################################################################		
def vipracing0(params):

	r = requests.get(url_vip)	
	data = r.content
	#plugintools.log("********************DATA: "+data+"***********************")	

	plugintools.add_item(action="",url="",title="[COLOR peru][B]  VipRacing[/B] [I](v0.01)[/I][/COLOR][COLOR yellow][I]    **** by Bad-Max ****[/I][/COLOR]",thumbnail=logo_vip,fanart=fondo_vip,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=logo_vip,fanart=fondo_vip, folder=False, isPlayable=False)

	canales = plugintools.find_single_match(data,'JSON.parse(.*?)navbar-nav').replace("\n","").replace('group":"' , 'COMIENZO')
	canales = canales.replace('group_name' , 'GRUPO').replace('name":"' , 'NOMBRE').replace('shortcut":"' , 'LINK')
	
	plugintools.add_item(action="canalesvip",title= "[COLOR red]-Canales para Eventos (Zapping)[/COLOR]", url="", extra="9", page=canales, thumbnail=logo_vip, fanart=fondo_vip, folder = True, isPlayable=False)
	plugintools.add_item(action="canalesvip",title= "[COLOR red]-Canales 24/7[/COLOR]", url="", extra="6", page=canales, thumbnail=logo_vip, fanart=fondo_vip, folder = True, isPlayable=False)
	plugintools.add_item(action="canalesvip", title="[COLOR red]-Canales Latinos[/COLOR]", url="", extra="7", page=canales, thumbnail=logo_vip, fanart=fondo_vip, folder = True, isPlayable=False)
	
	
def canalesvip(params):
	titulo = params.get("title")
	data = params.get("page")
	grupo = params.get("extra")
	
	plugintools.add_item(action="",url="",title=titulo,thumbnail=logo_vip,fanart=fondo_vip,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=logo_vip,fanart=fondo_vip, folder=False, isPlayable=False)
	
	if grupo == "9":  ## Canales Zaping
		canales = plugintools.find_multiple_matches(data,'ENZO9(.*?)COMI')		
	
	elif grupo == "6":  ## Canales 24/7
		canales = plugintools.find_multiple_matches(data,'ENZO6(.*?)COMI')		
	
	elif grupo == "7":  ## Canales Latinos
		canales = plugintools.find_multiple_matches(data,'ENZO7(.*?)COMI')		
	
	for item in canales:
	
		canal = plugintools.find_single_match(item,'NOMBRE(.*?)"')
		if len(canal) > 0:
			canal = "[COLOR white][B]" + canal + "[/COLOR][/B]"
			link = plugintools.find_single_match(item,'LINK(.*?)"')
			if len(link) > 0:
				link = url_vip + "channel/" + link
			
			url_montada = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url='+link+'%26referer='+url_vip
			plugintools.add_item(action="runPlugin", title=canal, url=url_montada, thumbnail=logo_vip, fanart=fondo_vip, folder = False, isPlayable=True)
			


	
	




			
			
#########################################################################		
######################### VerTelevisor.com Deportes #####################
#########################################################################		
def vertelevisor0(params):

	r = requests.get(url_tele)	
	data = r.content
	#plugintools.log("********************DATA: "+data+"***********************")	

	plugintools.add_item(action="",url="",title="[COLOR blue][B]  VerTelevisor.com Deportes[/B] [I](v0.01)[/I][/COLOR][COLOR yellow][I]    **** by Bad-Max ****[/I][/COLOR]",thumbnail=logo_tele,fanart=fondo_tele,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=logo_tele,fanart=fondo_tele, folder=False, isPlayable=False)

	canales = plugintools.find_single_match(data,'pagetitle">DEPORTES(.*?)id="categories-2')
	
	cadacanal = plugintools.find_multiple_matches(canales,'class="latestthumb(.*?)</a')
	for item in cadacanal:
		link = plugintools.find_single_match(item,'href="(.*?)"')
		titulo = plugintools.find_single_match(item,'alt="(.*?)"').replace("ver " , "").replace("Ver " , "").replace("VER " , "").title()
		sulogo = plugintools.find_single_match(item,'src="(.*?)"')
		if len(sulogo) == 0:
			el_logo = logo_tele
		else:
			el_logo = sulogo
	
		lareferencia = saca_ref(link)
		url_montada = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url='+link+'%26referer='+lareferencia
		plugintools.log("********************URL-Montada: "+url_montada+"***********************")	
		plugintools.add_item(action="runPlugin", title=titulo, url=url_montada, thumbnail=el_logo, fanart=fondo_tele, folder = False, isPlayable=True)
			


#########################################################################		
######################### VerPlusOnLine Deportes ########################
#########################################################################		
def verplus0(params):

	headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',"Origin":'http://verplusonline.com',"Referer": url_plus, "cookie": "aoc=a9c18614-6451-4ad8-841d-555f02590260"}
	
	r=requests.get(url_plus, headers=headers)
	data = r.content

	plugintools.add_item(action="",url="",title="[COLOR blue][B]           VerPlusOnline Deportes[/B] [I](v1.02)[/I][/COLOR][COLOR yellow][I]    **** by Bad-Max ****[/I][/COLOR]",thumbnail=logo_plus,fanart=fondo_plus,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=logo_plus,fanart=fondo_plus, folder=False, isPlayable=False)

	canales = plugintools.find_single_match(data,'pagetitle">(.*?)p><iframe')
	
	cadacanal = plugintools.find_multiple_matches(canales,'<a href=(.*?)/a>')
	for item in cadacanal:
		link = plugintools.find_single_match(item,'"(.*?)/"')

		if  'http://verplusonline.com' in link:
			headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',"Origin":'http://verplusonline.com',"Referer": link, "cookie": "aoc=a9c18614-6451-4ad8-841d-555f02590260"}
			r=requests.get(link, headers=headers)
			data2 = r.content  ## Nos vamos al salto para buscar el verdadero iframe

			titulo = plugintools.find_single_match(data2,'pagetitle">(.*?)<')
			if len(titulo) > 0:
				sulogo = plugintools.find_single_match(data2,'image" content="(.*?)"')
				if len(sulogo) == 0:
					el_logo = logo_plus
				else:
					el_logo = sulogo
					
				buscalink = plugintools.find_single_match(data2,'p><iframe(.*?)</iframe>')
				linkreal = plugintools.find_single_match(buscalink,'src="(.*?)"')
				lareferencia = saca_ref(linkreal)
				
				url_montada = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url='+linkreal+'%26referer='+lareferencia
				plugintools.log("********************URL-Montada: "+url_montada+"***********************")	
				plugintools.add_item(action="runPlugin", title=titulo, url=url_montada, thumbnail=el_logo, fanart=fondo_plus, folder = False, isPlayable=True)
			





def saca_ref(link):

	ref =  plugintools.find_single_match(link,'http://(.*?)/') 
	if len(ref) == 0:
		ref =  "https://" + plugintools.find_single_match(link,'https://(.*?)/') +"/"
	else:
		ref = "http://" + ref + "/"
	
	return ref
		
		
		
#########################################################################		
#########################DINOZAP#########################################
#########################################################################		
def dinozapmax0(params):

	r = requests.get(url_dino)	
	data = r.content

	plugintools.add_item(action="",url="",title="[COLOR blue][B]                 DinoZap[/B] [I](v1.02)[/I][/COLOR][COLOR yellow][I]    **** by Bad-Max ****[/I][/COLOR]",thumbnail=logo_dino,fanart=fondo_dino,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=logo_dino,fanart=fondo_dino, folder=False, isPlayable=False)

	periodo_agenda = plugintools.find_single_match(data,'Schedule(.*?)<')
	periodo_agenda = "[COLOR red][I]Agenda: " + periodo_agenda.strip().upper().replace("FROM","Desde el  ").replace("TO","  a el  ") + "[/I][/COLOR]"

	plugintools.add_item(action="dinozaping",url="",title="[COLOR skyblue]·····¿Hacemos DinoZapping?·····[/COLOR]",thumbnail=logo_zap,fanart=fondo_dino,folder=True,isPlayable=False)

	plugintools.add_item(action="",url="",title="",thumbnail=logo_dino,fanart=fondo_dino, folder=False, isPlayable=False)
	plugintools.add_item(action="",url="",title=periodo_agenda,thumbnail=logo_dino,fanart=fondo_dino, folder=False, isPlayable=False)
	
	r = requests.get(url_agenda_dino)	
	data = r.content
	
	fh = open(temp + "prog.txt", "wb")
	fh.write(data)
	fh.close()
	
	agendatxt = open(temp + "prog.txt",'r')
	lineas=agendatxt.readlines()
	agendatxt.close()

	accion = ""
	canal = ""
	for lin_actu in lineas:
		
		milinea = ""
		es_dia = False
		
		if lin_actu.upper().find("MONDAY") >= 0:
			milinea = "[COLOR lightgreen][B]···" + lin_actu.upper().replace("MONDAY","Lunes") + "···[/B][/COLOR]"
			es_dia = True

		elif lin_actu.upper().find("TUESDAY") >= 0:
			milinea = "[COLOR lightgreen][B]···" + lin_actu.upper().replace("TUESDAY","Martes") + "···[/B][/COLOR]"
			es_dia = True

		elif lin_actu.upper().find("WEDNESDAY") >= 0:
			milinea = "[COLOR lightgreen][B]···" + lin_actu.upper().replace("WEDNESDAY","Miercoles") + "···[/B][/COLOR]"
			es_dia = True

		elif lin_actu.upper().find("THURSDAY") >= 0:
			milinea = "[COLOR lightgreen][B]···" + lin_actu.upper().replace("THURSDAY","Jueves") + "···[/B][/COLOR]"
			es_dia = True

		elif lin_actu.upper().find("FRIDAY") >= 0:
			milinea = "[COLOR lightgreen][B]···" + lin_actu.upper().replace("FRIDAY","Viernes") + "···[/B][/COLOR]"
			es_dia = True

		elif lin_actu.upper().find("SATURDAY") >= 0:
			milinea = "[COLOR lightgreen][B]···" + lin_actu.upper().replace("SATURDAY","Sabado") + "···[/B][/COLOR]"
			es_dia = True

		elif lin_actu.upper().find("SUNDAY") >= 0:
			milinea = "[COLOR lightgreen][B]···" + lin_actu.upper().replace("SUNDAY","Domingo") + "···[/B][/COLOR]"
			es_dia = True
			
		elif lin_actu.upper().find("EMBED") >= 0:
			milinea = "[COLOR green][B]" + lin_actu.upper().replace("EMBED","Canal") + "[/B][/COLOR]"
			accion = "opciones_dino"
			lin_provi = lin_actu.upper()
			canal = plugintools.find_single_match(lin_provi,'EMBED (.*?)\t').replace("'","").replace('"','')
			canal = canal.replace("#","")
			
		else:
			hora = plugintools.find_single_match(lin_actu,'(.*?)\t')

			if len(hora) == 0:  # Es una linea en Blanco
				lin_actu = "XXXX"

			else:
				if len(hora) == 4:  # Le falta un 0 delante
					hora = "0" + hora

				hora = "[COLOR red]" + hora + "-> [/COLOR]"
					
				partido = plugintools.find_single_match(lin_actu,'\t(.*?)\t')
				partido = "[COLOR yellow]" + partido + "[/COLOR]"
				lin_actu = lin_actu.replace("(","DMO1").replace(")","DMO2")
				idioma = plugintools.find_single_match(lin_actu,'DMO1(.*?)DMO2')
				idioma = "[COLOR red][I]    [" + idioma + "] [/I][/COLOR]"
				
				milinea = hora + partido + idioma
		
		if accion == "" or es_dia == True:
			esreproducible = False
		else:
			esreproducible = True
			
		if lin_actu.upper().find("XXXX") >= 0:  # Para la linea de X q pone entre un día y otro y no sirve para nada
			hacer = "Nada"
		else:
			milinea = milinea.replace("\t","").replace("\n","")
			
			if es_dia == True:
				plugintools.add_item(action="", title=milinea, url="", thumbnail=logo_dino,fanart=fondo_dino, folder = False, isPlayable=False)
			else:
				plugintools.add_item(action=accion, title=milinea, url=canal, thumbnail=logo_dino,fanart=fondo_dino, folder = True, isPlayable=False)
		
			
			
def dinozaping(params):			
	thumbnail = params.get("thumbnail")
	fanart = params.get("fanart")

	plugintools.add_item(action="",url="",title="[COLOR blue][B]                 DinoZapping[/B][/COLOR]",thumbnail=thumbnail,fanart=fanart,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=thumbnail, fanart=fanart, folder=False, isPlayable=False)

	canal=111
	while canal <= 200:
			
		plugintools.add_item(action="opciones_dino", title="Zapping canal "+str(canal), url=str(canal), thumbnail=thumbnail, fanart=fanart, folder = True, isPlayable=False)
		canal = canal + 1
		

		
		
def opciones_dino(params):
	thumbnail = params.get("thumbnail")
	fanart = params.get("fanart")
	titulo = params.get("title")
	milinea = params.get("title")
	canal = params.get("url")

	if "Zapping" in titulo:
		hacer = "Nada"
	else:	
		plugintools.add_item(action="",url="",title=milinea,thumbnail=thumbnail,fanart=fanart,folder=False,isPlayable=False)
		plugintools.add_item(action="",url="",title="**Paciencia, pueden tardar en cargar... Si tarda mucho, haz click una 2ª Vez**",thumbnail=thumbnail,fanart=fanart,folder=False,isPlayable=False)
		plugintools.add_item(action="",url="",title="",thumbnail=thumbnail, fanart=fanart, folder=False, isPlayable=False)

	if "Zapping" in titulo:
		titulo2 = titulo + " ...Opción SunHD"
	else:
		titulo2 = "Ver Evento de Canal " + canal + " ...Opción SunHD"

	enlace = "http://www.sunhd.info/channelsa.php?file=" + canal + "&width=650&height=450&autostart=true"
	url_montada = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url='+enlace+'%26referer='+"http://www.sunhd.info/"
	plugintools.add_item(action="runPlugin", title=titulo2, url=url_montada, thumbnail=thumbnail, fanart=fanart, folder = False, isPlayable=True)

	if "Zapping" in titulo:
		titulo2 = titulo + " ...Opción DinoZap"
	else:
		titulo2 = "Ver Evento de Canal " + canal + " ...Opción DinoZap"

	enlace = "http://www.dinozap.info/redirect/channel.php?id=" + canal + "&width=650&height=450&autostart=true"
	url_montada = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url='+enlace+'%26referer='+"http://www.dinozap.info/"
	plugintools.add_item(action="runPlugin", title=titulo2, url=url_montada, thumbnail=thumbnail, fanart=fanart, folder = False, isPlayable=True)

		
		
		
#########################################################################################################################		
######################################### VerLiga.net ###################################################################
#########################################################################################################################		

def verliganet0(params):
	plugintools.log("[%s %s] http://wwww.verliga.net %s " % (addonName, addonVersion, repr(params)))
	logo = logo_verliga
	fondo = fondo_verliga

	plugintools.add_item(action="",url="",title="[COLOR blue][B]                 VerLiga.net[/B]   [I]"+version_verliga+"[/I][/COLOR][COLOR yellow][I]    **** byBad-Max ****[/I][/COLOR]",thumbnail=logo_verliga,fanart=fondo_verliga,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=logo_verliga, fanart=fondo_verliga, folder=False, isPlayable=False)
	
	r = requests.get(url_verliga)	
	data = r.content

	plugintools.add_item(action="zapliga",url=data,title="[COLOR orange][B]-Hacer Zapping de Canales-[/COLOR][/B]",thumbnail=logo_zap, fanart=fondo_verliga, folder=True, isPlayable=False)

	#vamos a agrupar la agenda x dias
	agenda = plugintools.find_multiple_matches(data,'p><center><h3(.*?)</tbody')
	

	for item in agenda:
		dia = "[COLOR orange]   ***" + plugintools.find_single_match(item,'>(.*?)<') + "***[/COLOR]"
		plugintools.add_item(action="",url="",title=dia,thumbnail="http://i.imgur.com/fsnLX0I.png",fanart=fondo_verliga,folder=False,isPlayable=False)

		eventos = plugintools.find_multiple_matches(item,'<span class="t(.*?)/a>')
		
		for evento in eventos:
			hora = "[COLOR red][B][I](" + plugintools.find_single_match(evento,'>(.*?)<') + "h)->[/B][/I][/COLOR]"
			partido = "[COLOR green][B](" + plugintools.find_single_match(evento,'<strong>(.*?)</td') + "h)[/B][/COLOR]"
			partido = partido.replace("</strong>" , "")
			link =  plugintools.find_single_match(evento,'href="(.*?)"')
			logo =""
			logo =  plugintools.find_single_match(evento,'src="(.*?)"')
			if len(logo) == 0:
				logo = thumbnail
			
			linea = hora + partido
			linea = linea.replace("h)",")")

			url_montada = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='+link+"%26icon%3d"+logo+'%26referer='+url_ref_verliga
			plugintools.add_item(action="runPlugin",title=linea,url=url_montada,thumbnail=logo_verliga,fanart=fondo_verliga,folder=False,isPlayable=True)
			


def zapliga(params):
	data = params.get("url")
			
	canales = plugintools.find_single_match(data,'selected">PROGRAMACION(.*?)</ul>')
	cadacanal = plugintools.find_multiple_matches(canales,'href="http://www.verliga.net(.*?)/a></li>')
	
	for item in cadacanal:
		link = "http://www.verliga.net/" + plugintools.find_single_match(item,'/(.*?)"')
		canal = plugintools.find_single_match(item,'>(.*?)<')
		canal = "-Ir a " + canal
		
		url_montada = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='+link+"%26icon%3d"+logo_zap+'%26referer='+url_ref_verliga
		plugintools.add_item(action="runPlugin",title=canal,url=url_montada,thumbnail=logo_zap,fanart=fondo_verliga,folder=False,isPlayable=True)

			
		
		
		
def runPlugin(params):
	url = params.get("url")

	builtin = 'RunPlugin(%s)' %url
	xbmc.executebuiltin(builtin)   


		
		
		
		
run()




	

