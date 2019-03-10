import ocr
import webbrowser
from selenium import webdriver
import pyscreenshot as ImageGrab

import json
import urllib.request as urllib2
from bs4 import BeautifulSoup

from PIL import Image
import pytesseract



#from edge of blue add 216 down


# YOU NEED TO BE LOGGED IN BFEOREHAND BOTH ON MAC AND IPHONE
#webbrowser.open('https://www.shazam.com/myshazam')

#browser = webdriver.Chrome()

#browser.get("https://www.shazam.com/myshazam")

def screenshot(x1,y1,x2,y2):

	image = ImageGrab.grab(bbox=(x1, y1, x2, y2))  # X1,Y1,X2,Y2
	return image

def songseparate(pathway):
	x = 550
	y = 280
	im = Image.open(pathway)
	pix = im.load()
	while str(pix[x,y]) == str("(0, 205, 255, 255)"):
		print(im.size)  # Get the width and hight of the image for iterating over
		print(pix[x, y])  # Get the RGBA Value of the a pixel of an image
		y += 1
		print("y: ", y)
	startingy = y + 216
	
	songpic = screenshot(153, startingy, 650, startingy+104)




	#pix[x, y] = value  # Set the RGBA Value of the image (tuple)

songseparate("/Users/teddy/Desktop/test6.png")



