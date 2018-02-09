import pylast
import json

class LastFMFetcher:

	def __init__(self):
		with open("./resources/account",'r') as account_file:
			dict_info=json.load(account_file)
			self.network=pylast.LastFMNetwork(**dict_info)	
		#
	
	def extract(itr,attr):
		return [item[0].__getattribute__(attr) for item in itr]
	
	def getArtist(self,artist_name):
		return pylast.Artist(artist_name,self.network)
	
	def getTrack(self,artist_name,title):
		return self.network.get_track(artist_name,title)
		
	def topTracks(self,artist_name):
		return [i[0].title for i in self.getArtist(artist_name).get_top_tracks()]
		
	def getAlbum(self,artist_name,album_name):
		return self.network.get_album(artist_name,album_name)
		
	def getSimilarArtist(self,artist_name):
		return self.getArtist(artist_name).get_similar()
		
	def getSimilarTrack(self,artist_name,title):
		return self.getTrack(artist_name,title).get_similar()