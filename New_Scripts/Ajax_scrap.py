from bs4 import BeautifulSoup
import os
import requests
from selenium import webdriver
import shutil
import time

url = "https://fossbytes.com/"

driver = webdriver.Firefox()
driver.get(url)

iteration = 0
while iteration < 2:
	html = driver.execute_script("return document.documentElement.outerHTML");
	sel_soup = BeautifulSoup(html, "html.parser")
	print(len(sel_soup.findAll('img')))

	images = []
	for image in sel_soup.findAll('img'):
		src = image["src"]
		images.append(src)

	for img in images:
		try:
			img_req = requests.get(img,stream=True)
			filename = os.path.basename(img)
			path = os.path.join(os.getcwd(),"images", filename)
			with open(path, "wb") as file:
				shutil.copyfileobj(img_req.raw, file)
			del img_req
		except:
			pass
	iteration += 1
	time.sleep(5)