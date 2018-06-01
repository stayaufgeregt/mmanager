#!/usr/bin/python3
print("Loading...")
import download
import database
import menu
import subprocess
import time
import playlist
print("Done")

def musics_on_demand(downloader):
	while True:
		request=input("What do you want to listen to ? ")

		if request in ("","stop","quit","q","exit"):
			break;

		#
		print("Downloading...")
		downloader.download(request)
		print("Music downloaded")
	return
	

def change_ytdl_params(downloader):
	
	params=downloader.getParams()
	
	menu_list=list(map(lambda param_name:(param_name,lambda:param_name),params))
	menu_list.append( ("add new parameter",lambda:"add parameter") )
	menu_list.append( ("<-- main menu",lambda:"return") )
	
	choice=menu.Menu("Youtube-dl parameters",menu_list)
	
	if choice=="return":
		return
	elif choice=="add parameter":
		param_name=input("Parameter name : ")
		param_value=input("Parameter value : ")
		downloader.setParam(param_name,param_value)  #type of new field needs fix
	else:
		print(choice," : ",downloader.getParams()[choice])
		new_value=input("New value : ")
		downloader.setParam(choice,type(params[choice])(new_value))	#cast in the same type as before
		
	#

def save_ytdl_params(downloader):
	downloader.saveParam()
	input("SAVED SUCCESSFULLY")
	#

def play(curPlaylist,dler):
	
	code=None
	
	while code==None:
		songPath=dler.getParams()["musicdir"]+curPlaylist.song
		media_process=subprocess.Popen('play-audio "'+songPath+'"',shell=True)	#opened in bg
		
		code=menu.Menu(str(curPlaylist.songID)+" : "+curPlaylist.song[:36],[("Next : "+curPlaylist.next[:24],lambda:curPlaylist.change(1)),\
																("Prev : "+curPlaylist.prev[:24],lambda:curPlaylist.change(-1)),\
																("Quit",lambda:0)])
		#
		if media_process.poll()==None:
			media_process.terminate()
	#
def shuffle(curPlaylist):
	curPlaylist.shuffle()
	input("[Playlist shuffled]")
	
def blindtest(curPlaylist,dler):
	blindtest_pl=curPlaylist.sample(10)
	print("\nStarting blindtest :\n")
	for i in range(blindtest_pl.songNB):
		songPath=dler.getParams()["musicdir"]+blindtest_pl.song
		media_process=subprocess.Popen('play-audio "'+songPath+'"',shell=True)	#opened in bg
		time.sleep(15)
		print(str(i)+" : "+blindtest_pl.song)
		if media_process.poll()==None:
			media_process.terminate()
		blindtest_pl.change(1)
	
	time.sleep(5)
	#
if __name__=='__main__':
	dler=download.Downloader()
	#network=database.LastFMFetcher()
	curPlaylist=playlist.Playlist(downloader=dler)

	
	while "exit"!=menu.Menu("Pyplayer 0.0",[("Play current playlist",lambda:play(curPlaylist,dler)),\
											("Download music",lambda:musics_on_demand(dler)),\
											("Change parameters",lambda:change_ytdl_params(dler)),\
											("Save parameters",lambda:save_ytdl_params(dler)),\
											("shuffle playlist",lambda:shuffle(curPlaylist)),\
											("blindtest",lambda:blindtest(curPlaylist,dler)),\
											("Quit",lambda:"exit")]):
		pass
	
	#print(network.getSimilarTrack("limpbizkit","behind blue eyes"));

	
	#print(top_tracks(network,input("Artist name : ")))