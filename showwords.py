import time
import random
import notify2

wordfile = open('words.text','r')

def show(tile,message):
	notify2.init('start')
	notific = notify2.Notification(word,meaning)
	notific.show()

#while 1:
for words in wordfile:
	word,meaning= words.rstrip().split('-')
	show(word,meaning)
	time.sleep(10)