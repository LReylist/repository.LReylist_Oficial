# -*- coding: utf-8 -*-
#--------------------------------------------------------
#  creado por quequeQ para PalcoTV
# (http://forum.rojadirecta.es/member.php?1370946-quequeQ)
# (http://xbmcspain.com/foro/miembro/quequino/)
# Version 0.0.3 (01.11.2014)
#--------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
#--------------------------------------------------------

import os,sys,urlparse,urllib,urllib2,re,shutil,zipfile,cookielib
import xbmc,xbmcgui,xbmcaddon,xbmcplugin
import plugintools


def frame_parserl(params):
	url = params.get("url")
	print "START="+params.get("url")
	if params.get("title")=="[COLOR=red]Pon[COLOR=yellow]Tu[COLOR=red]Canal[/COLOR][/COLOR][/COLOR]" :
	 pattern1 = 'popUp\(\'([^\']+).*src="([^"]+)'
	 pattern2 = "http://canalesgratis.me/canales/"#http://canalesgratis.me/canales/ant3op2.php
	 pattern3 = ".php"
	else :#PonLaTele
	 pattern1 = 'popUp\(\'([^\']+).*src="([^"]+)'
	 pattern2 = "http://verdirectotv.com/canales/"
	 pattern3 = ".html"
	request_headers=[]
	request_headers.append(["User-Agent","Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)"])
	body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
	data=body
	ref = url
	matches = find_multiple_matches_multi(data,pattern1)
	i=0
	for scrapedurl, scrapedthumbnail in matches:
		thumb = scrapedthumbnail
		url = urlparse.urljoin( params.get("url") , scrapedurl.strip() )
		import string
		title = url.replace(pattern2,"").replace(pattern3,"").replace("-"," ");title = string.capwords(title)
		if i%2==0:
		 p1 = title[0]
		 p2 = "[COLOR=red]"+title[0]+"[/COLOR]"
		 title = title.replace(p1,p2);
		else:
		 p1 = title[0]
		 p2 = "[COLOR=yellow]"+title[0]+"[/COLOR]"
		 title = title.replace(p1,p2);
		i+=1
		msg = "Resolviendo enlace ... "
		uri = url+'@'+title+'@'+ref
		plugintools.add_item( action="frame_parser2" , title=title , url=uri ,thumbnail=thumb ,fanart=thumb , isPlayable=True, folder=False )
		
def frame_parser2(params):
	#regex='<iframe.*?src="([^\'"]*).*?<\/iframe>|"window\.open\(\'([^\']+)'#en futuras versiones
	regex='<iframe.*?src="([^\'"]*).*?<\/iframe>'
	url,title,thumbnail = params.get("url"),params.get("title"),params.get("thumbnail")
	url=url.split('@');title=url[1];ref=url[2];url=url[0];
	body='';bodyi=[];urli=[];bodyy='';enctrdiy=[];enctrdi=[];urlo=[url];
	i=0;j=len(urlo);urli=[url];
	while i < j:
	 ref=urli[i];
	 url=urlo[i];
	 try:
	  curl_frame(url,ref,body,bodyi,bodyy,urli);
	 except:
	  pass
	 bodyy=' '.join([str(y) for y in bodyi]);
	 enctrd=find_multiple_matches_multi(bodyy,regex);enctrd=list(set(enctrd))
	 for q in enctrd:
	  if q not in urlo:urlo[len(urlo):]=[q];urli[len(urli):]=[url];
	 j=len(urlo);i+=1;
	 try:
	  jscalpe(bodyy,url,ref)
	 except:
	  pass
	print "LIST OF URL's=",urli;
	#jscalpe(bodyy,url,ref)#cambiar comment con linea jscalpe anterior

def jscalpe(bodyy,url,ref):
	p=('m3u8','freelivetv','freetvcast','goo\.gl','vercosasgratis','byetv','9stream','castalba','direct2watch','kbps','flashstreaming','cast247','ilive','freebroadcast','flexstream','mips','veemi','yocast','yukons','ilive','iguide','ucaster','ezcast','plusligaonline','tvonlinegratis');z=len(p);
	for i in range(0, z):
	 regex='<script.*?('+str(p[i])+').*?<\/script>'
	 caster=[];
	 enctrd=plugintools.find_single_match(bodyy,regex);
	 #!!!Quita el "if" de abajo para ver todo los "enctrd" encontrados de cada "p" caster !!!
	 if len(enctrd)>0:
	  caster=''.join(map(str,enctrd));
	  print caster;
	  import re
	  r = re.compile('(<script.*?(?=>)>(.*?)(?=<))?.*?src=\'?"?(.*?'+caster+'[^\'",;]+)', re.VERBOSE)
	  res = re.findall(r,bodyy);
	  if caster.find('m3u8') >=0:
	   r = 'file=(.*?m3u8)'
	   res = plugintools.find_single_match(bodyy,r);
	   res=filter(None,res);res=str(res);script='';
	   nstream(url,ref,caster,res,script)
	  else:
	   res=filter(None,res);#print res
	  res=list(set(res));
	  script=''.join(map(str,res));
	  nstream(url,ref,caster,res,script)

def curl_frame(url,ref,body,bodyi,bodyy,urli):
	request_headers=[];
	request_headers.append(["User-Agent","Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)"])
	request_headers.append(["Referer",ref])
	try:
	 body,response_headers=plugintools.read_body_and_headers(url, headers=request_headers);
	 bodyi+=([body]);
	except:
	 #ACTIVATE LINE (print in try) to view headers and errors!!!
	 pass

def find_multiple_matches_multi(text,pattern):
    matches = re.findall(pattern,text, re.MULTILINE)
    return matches	