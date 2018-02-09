import os
import curses
from curses import wrapper


def Menu(title,options):

	
	output=None
	
	def main(stdscreen):
		nonlocal output
		
		currentline=0
		
		curses.noecho() #do not display keys on screen
		curses.cbreak()
		stdscreen.keypad(True)

		stdscreen.clear()
		stdscreen.addstr(0,1,title,curses.A_UNDERLINE)
		
		for i in range(len(options)):
			stdscreen.addstr(i+2,1,"{}  -  {}".format(i+1,options[i][0]))
			
		stdscreen.addstr(currentline+2,1,"{}  -  {}".format(currentline+1,options[currentline][0]),curses.A_REVERSE)
		stdscreen.refresh()
		
		pressed_key=curses.KEY_MIN
		
		while pressed_key!=curses.KEY_ENTER and pressed_key!=ord('\n'):
		
			pressed_key=stdscreen.getch()
			
			stdscreen.addstr(currentline+2,1,"{}  -  {}".format(currentline+1,options[currentline][0]))

			if pressed_key==curses.KEY_UP:
				currentline=currentline-1
			elif pressed_key==curses.KEY_DOWN:
				currentline=currentline+1
			currentline%=len(options)
			
			stdscreen.addstr(currentline+2,1,"{}  -  {}".format(currentline+1,options[currentline][0]),curses.A_REVERSE)
			stdscreen.refresh()
		curses.nocbreak()
		stdscreen.keypad(False)
		curses.echo()
		curses.endwin()
		output=options[currentline][1]()
	wrapper(main)
	return output

	

if __name__=='__main__':
	quit=lambda :None
	menu2=lambda :Menu("Menu 2", [ ("quitter",quit), ("menu1",menu1) ])
	menu1=lambda :Menu("Menu 1",[ ("menu2",menu2) , ("quitter",quit) ])

	menu1()