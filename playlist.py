import os
import random

AUDIO_FORMATS=['m4a','mp3','wav']
def format(s):
	if len(s)<5:
		return False
	if s[-4]!='.':
		return False
	if s[-3:] in AUDIO_FORMATS:
		return True
		
	return False
	
class Playlist:
	
	def __init__(self,**kwargs):
		
		self.playlist=None
		self.songID=None
		self.load(**kwargs)	
	#
	
	def load(self,**kwargs):
		
		if kwargs.get("downloader"):
			self.playlist=list(filter(format,os.listdir(kwargs["downloader"].getParams()["musicdir"])))
		elif kwargs.get("playlist"):
			self.playlist=kwargs["playlist"]
			
		self.songID=0
		self.songNB=len(self.playlist)

		
	#
	def empty(self):
		return self.playlist is None or self.songNB<=0
		
	@property
	def song(self):
		return self.playlist[self.songID]
	@property
	def next(self):
		return self.playlist[(self.songID+1)%self.songNB]
	@property
	def prev(self):
		return self.playlist[(self.songID-1)%self.songNB]
	#
	
	def change(self,val):
		self.songID=(self.songID+val)%self.songNB
	def shuffle(self):
		random.shuffle(self.playlist)
		self.songID=0
	#
	
		
	def sample(self,n):
	
		if n>self.songNB:
			print("You need at least {} songs, you currently have {} songs.".format(n,self.songNB))
			n=self.songNB
		return	Playlist(playlist=random.sample(self.playlist,n))

	#