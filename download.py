import youtube_dl as yt
import json
import os.path

DEFAULT_CONFIG="""{"noplaylist": 1, "format": "m4a","default_search": "ytsearch1", "musicdir": "../music/", "outtmpl": "../music/%(title)s.%(ext)s", "nocheckcertificate": false, "extractaudio": 1}"""
			
class Downloader:


	def __init__(self):
		
		if not(os.path.exists("./resources/downloaderConfig")):
			with open("./resources/downloaderConfig",'w') as cfg:
				cfg.write(DEFAULT_CONFIG)
				
		with open("./resources/downloaderConfig",'r') as config_file:
			dict_config=json.load(config_file)
			self.downloader=yt.YoutubeDL(dict_config)	
		#
		
		
	def download(self,request):
		self.downloader.download([request])
		
	def getParams(self):
		return self.downloader.params
		
	def setParam(self,param_name,param_value):
		self.downloader.params[param_name]=param_value
		
	def saveParam(self):
		
		with open("./resources/downloaderConfig",'w') as config_file:
			json.dump(self.getParams(),config_file)
		#