import os
import sys
import time
from termcolor import colored

    
def fbanner():
	try:
		os.system("cd .web/fb_standard && ./fbs")
	except KeyboardInterrupt:
		print(colored("are you want to check result", 'green'))
		os.system("cat .web/fb_standard/cat.txt && rm -rf .web/fb_standard/cat.txt")
		time.sleep(6)
		sys.exit()

		
def gmailb():
	try:
		os.system("cd .web/google_standard && ./gs")
	except KeyboardInterrupt:
	    print(colored("are you want to check result", 'green'))
	    os.system("cat .web/google_standard/cat.txt && rm -rf .web/google_standard/cat.txt")
	    time.sleep(6)
	    sys.exit()
		
def fbab():
	try:
		os.system("cd .web/fb_advanced_poll && ./fba")
	except KeyboardInterrupt:
		print(colored("are you want to check results", 'green'))
		os.system("cat .web/fb_advanced_poll/cat.txt && rm -rf .web/fb_advanced_poll/cat.txt")
		time.sleep(6)
		sys.exit()

def Update():
	os.system("git pull")
	restartprogram()

def restartprogram():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
