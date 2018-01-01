#!/usr/bin/python3
print("Loading...")
import download
import database
import menu

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
	
	param_list=[ (param_name,lambda:param_name) for param_name in downloader.getParams() ]
	param_list.append( ("add parameter",lambda:"add parameter") )
	param_list.append( ("return to main menu",lambda:"return") )
	
	choice=menu.Menu("Youtube-dl parameters",param_list)
	
	if choice=="return":
		return
	elif choice=="add parameter":
		param_name=input("Parameter name : ")
		param_value=input("Parameter value : ")
		
		downloader.setParam(param_name,param_value)
	else:
		print("Previous value : ",downloader.getParams()[choice])
		param_value=input("New value : ")
		downloader.setParam(choice,param_value)
		
	#



def save_ytdl_params(downloader):
	pass

	
if __name__=='__main__':
	dler=download.Downloader()
	#network=database.LastFMFetcher()

	while "exit"!=menu.Menu("Pyplayer 0.0",[("Download music",lambda:musics_on_demand(dler)),("Change parameters",lambda:change_ytdl_params(dler)),("Quit",lambda:"exit")]):
		pass
	
	#print(network.getSimilarTrack("limpbizkit","behind blue eyes"));

	
	#print(top_tracks(network,input("Artist name : ")))