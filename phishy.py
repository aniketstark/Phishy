import os
import sys
from core.starkcore import *
from time import sleep as timeout
from termcolor import colored

def menu():

    print(colored("""

 .########..##.....##.####..######..##.....##.##....##
 .##.....##.##.....##..##..##....##.##.....##..##..##.
 .##.....##.##.....##..##..##.......##.....##...####..
 .########..#########..##...######..#########....##...
 .##........##.....##..##........##.##.....##....##...
 .##........##.....##..##..##....##.##.....##....##...
 .##........##.....##.####..######..##.....##....##...
 
                                                      
>>>>>>created by aniket stark    
>>>>>> Aniketstark tech (youtube channel)
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
		Facebook()
	elif stark == "2":
		FacebookA()
	elif stark == "3":
		Gmail()
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
