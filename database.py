import pylast

class LastFMFetcher:

	def __init__(self):
		try:
			account_file=open("./resources/account",'r')
			dict_info=eval('{'+(','.join(account_file.readlines()))+'}')
			self.network=pylast.LastFMNetwork(**dict_info)
			account_file.close()
			return
		except IOError as e:
			print(e)
			print("Lastfm account file missing at ./resources/")
			exit(-1)
		return
	
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