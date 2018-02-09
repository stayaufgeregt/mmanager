import youtube_dl as yt
import json

class Downloader:


	def __init__(self):
		
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