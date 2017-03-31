                					####Python Script to get the words and it's meaning####

import requests
import bs4 as bs

url = 'https://www.vocabulary.com/lists/558097'

req = requests.get(url)



soup = bs.BeautifulSoup(req.content,'lxml')
contents = soup.find('div',{'class':'content-wrapper'})
contents_entry = contents.find('ol',{'class':'wordlist notesView'}).find_all('li')

									####creating the file of words and meaning######## 

wordfile = open('words.text','a')
for entry in contents_entry:
	word = entry.find('a').text
	meaning = entry.find('div').text
	wordfile.write(word)
	wordfile.write('-')
	wordfile.write(meaning)
	wordfile.write('\n')	

wordfile.close()
