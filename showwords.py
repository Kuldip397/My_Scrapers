			####Python Script to show words with meanings through Dekstop notification#####    
import time
import random
import notify2

			####First create the file words.text,which I've created through getwords.py####

wordfile = open('words.text','r')

				####Function to create dekstop notification####

def show(tile,message):
	notify2.init('start')
	notific = notify2.Notification(word,meaning)
	notific.show()

	                    ####Reading the file for words and meanings after 10 seconds####
		
for words in wordfile:
	word,meaning= words.rstrip().split('-')
	show(word,meaning)
	time.sleep(10)
