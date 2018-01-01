import youtube_dl as yt

class Downloader:


	def __init__(self):
		self.downloader=None
		
		try:
			config_file=open("./resources/downloaderConfig",'r')
			dict_config=eval('{'+(','.join(config_file.readlines()))+'}')
			self.downloader=yt.YoutubeDL(dict_config)
			config_file.close()
			return
		except IOError as e:
			print(e)
			print("YoutubeDL config file missing at ./resources/")
			exit(-1)
			
		return
		
		
	def download(self,request):
		self.downloader.download([request])
		
	def getParams(self):
		return self.downloader.params
		
	def setParam(self,param_name,param_value):
		self.downloader.params[param_name]=param_value