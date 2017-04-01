									####Python Scripts to sort the movies according to their IMDM rating####


import os
import requests
import bs4 as bs
import re
									          ####Function to return the rating of the movie####

def get_rating(link):
	try:
		comp_link = 'https://www.imdb.com'+link
		req2 = requests.get(comp_link)
		soup2 = bs.BeautifulSoup(req2.content,'lxml')
		rating = soup2.find('div',{'class':'ratingValue'}).find('strong').find('span').text
		return rating
	except:
		print ('XXXXXXX NO SUCH NAME EXIST.....ENTER THE VALID NAME OF DIRECTORY XXXXXXXX')

		
										
dirctries= []
for i,j,k in os.walk(os.getcwd()):
	dirctries.append(j)
dirctries = dirctries[0]
new_dirs = []
for dirctry in dirctries:
	new_dir = (" ".join(re.findall('[a-zA-z ]+',dirctry))).strip()
	os.rename(dirctry,(" ".join(re.findall('[a-zA-z ]+',dirctry))).strip())
	dirctry = new_dir
	new_dirs.append(new_dir)
	print(dirctry)
	

print ('Sorting.......')
rating = []
for name in new_dirs:
	url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q={}&s=all'.format(name)

	req = requests.get(url)
	soup = bs.BeautifulSoup(req.content,'lxml') 
	
	
	search_link = soup.find('div',{'class':'findSection'}).find('table').find('tr')
	
	link = search_link.find('a').get('href')


	
	rating.append(get_rating(link))

for n,dirctry in enumerate(new_dirs):
	os.rename(dirctry,rating[n]+' '+dirctry)

print ('DONE')	