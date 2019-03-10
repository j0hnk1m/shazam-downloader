import ocr
import webbrowser
from selenium import webdriver
import pyscreenshot as ImageGrab


# YOU NEED TO BE LOGGED IN BFEOREHAND BOTH ON MAC AND IPHONE
webbrowser.open('https://www.shazam.com/myshazam')
browser = webdriver.Chrome()
browser.get("https://www.shazam.com/myshazam")

def screenshot():

	image = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2



