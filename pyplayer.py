#!/usr/bin/python3
print("Loading...")
import download
import database
import menu
import os
import subprocess
print("Done")

currentPlaylist=None
songId=None

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
def random_playlist(downloader):
	global currentPlaylist
	global songId
	
	currentPlaylist=list(filter(lambda s:s[-4:]==".m4a",os.listdir(downloader.getParams()["musicdir"])))
	songId=0
	#

def save_ytdl_params(downloader):
	downloader.saveParam()
	input("SAVED SUCCESSFULLY")
	#

def play(downloader):
	
	global currentPlaylist
	global songId
	if currentPlaylist==None or songId==None:
		print("Please, create playlist first")
		return
	
	code=1
	
	while code!=0:
		songPath=downloader.getParams()["musicdir"]+currentPlaylist[songId]
		media_process=subprocess.Popen(['play-audio '+songPath,''],shell=True)	#opened in bg
		
		code=menu.Menu(str(songId)+": "+currentPlaylist[songId],[("Prev : "+currentPlaylist[songId-1][:16],lambda:-1),\
																("Next : "+currentPlaylist[(songId+1)%len(currentPlaylist)][:16],lambda:1),\
																("Quit",lambda:0)])
		#
		if media_process.poll()==None:
			media_process.terminate()
		songId=(songId+code)%len(currentPlaylist)
	
if __name__=='__main__':
	dler=download.Downloader()
	#network=database.LastFMFetcher()

	while "exit"!=menu.Menu("Pyplayer 0.0",[("Download music",lambda:musics_on_demand(dler)),\
											("Change parameters",lambda:change_ytdl_params(dler)),\
											("Save parameters",lambda:save_ytdl_params(dler)),\
											("Random playlist",lambda:random_playlist(dler)),\
											("Play current playlist",lambda:play(dler)),\
											("Quit",lambda:"exit")]):
		pass
	
	#print(network.getSimilarTrack("limpbizkit","behind blue eyes"));

	
	#print(top_tracks(network,input("Artist name : ")))