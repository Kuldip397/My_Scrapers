							####Python Script to find the IMDB rating of movies and TV series#####

import requests 
import bs4 as bs

						####Function to confirm the name of movie or Tv series to get the correct rating####

def cnfm_page(link):
	try:
		name_link = 'https://www.imdb.com'+link
		req2 = requests.get(name_link)
		soup2 = bs.BeautifulSoup(req2.content,'lxml')
		title = soup2.find('div',{'class':'title_wrapper'}).find('h1')
		plot = soup2.find('div',{'class':'plot_summary_wrapper'}).find('div',{'class','summary_text'})
		print (title.text)
		print ('With plot: {}'.format(plot.text.strip())) 
		ret = input('Is this what you are searching for(yes or no): ')
		if ret=='yes' or ret=='Yes':
			return True
		if ret=='no' or ret=='No':
			return False
	except:
		print ('XXXXXXX NO SUCH NAME EXIST.....ENTER THE VALID NAME XXXXXXXX')
		exit()		

					####funtion to get the rating after the confirmation of movie or Tv series name####

def getrating(link):
	try:
		comp_link = 'https://www.imdb.com'+link
		req3 = requests.get(comp_link)
		soup3 = bs.BeautifulSoup(req3.content,'lxml')
		rating = soup3.find('div',{'class':'ratingValue'}).find('strong')['title']
		return rating
	except:
		print ('XXXXXXX NO SUCH NAME EXIST.....ENTER THE VALID NAME XXXXXXXX')
		exit()		



name = input("Enter the movie or TV series name: ")

url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q={}&s=all'.format(name)

req = requests.get(url)
soup = bs.BeautifulSoup(req.content,'lxml') 

search_links = soup.find('div',{'class':'findSection'}).find('table').find_all('tr')# this will give the list of all possible links for the given name

Slinks_list = []
for link in search_links:
	Slinks_list.append(link.find('a').get('href'))


for link in Slinks_list:
	val =cnfm_page(link)
	if val is True:
		break;	

req_link = link #link of the movie ,which we are looking for
 
rating = getrating(req_link)
print ('Rating-- {}'.format(rating))