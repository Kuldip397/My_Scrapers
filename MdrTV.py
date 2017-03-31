import requests
import bs4 as bs

url = 'https://www.youtube.com/user/elMadridistaTV/videos'

req = requests.get(url)
soup = bs.BeautifulSoup(req.content,'lxml')

vidoes = soup.find('div',{'class':'branded-page-v2-body branded-page-v2-primary-column-content'})
vlist = vidoes.find('ul',{'id':'browse-items-primary'}).find('ul',{'class':'channels-browse-content-grid branded-page-gutter-padding grid-lockups-container'})
video = vlist.find('li').find('div',{'class':'yt-lockup-content'}).find('a')
videolink = video.get('href')

dwnpage_link = 'https://www.keepvid.com/?url=https://www.youtube.com{}'.format(videolink)
req2 = requests.get(dwnpage_link)
soup2 = bs.BeautifulSoup(req2.content,'lxml')
title = soup2.find('div',{'id':'info'}).find('div',{'class':'text'}).find('h3').text
Qualities= soup2.find('div',{'id':'dl'}).find('dl').find_all('dd')
quality = input('Enter the quality in which you want to download the video ')
if(quality == '720p'):
	link = Qualities[0].find('a').get('href')
if(quality == '480p'):
	link = Qualities[1].find('a').get('href')
if(quality == '240p'):
	link = Qualities[2].find('a').get('href')
if(quality == '144p'):
	link = Qualities[3].find('a').get('href')			
title =title+'.mp4'
req3 =requests.get(str(link))
with open(title,'wb') as myfile:
	myfile.write(req3.content)