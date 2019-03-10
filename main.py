import ocr
import music
import webbrowser
import pyscreenshot
import pyautogui
import time
from PIL import Image
import pytesseract


# YOU NEED TO BE LOGGED IN BFEOREHAND BOTH ON MAC AND IPHONE
webpage = webbrowser.open('https://www.shazam.com/myshazam')
time.sleep(2)
pyautogui.scroll(-3)
time.sleep(2)
pyautogui.scroll(-2)
time.sleep(2)
pyautogui.scroll(-3)
time.sleep(2)
pyautogui.scroll(-2)



def screenshot(x1,y1,x2,y2):

	image = pyscreenshot.grab(bbox=(x1, y1, x2, y2))  # X1,Y1,X2,Y2
	return image


def song_separate(pathway):
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
