import ocr
import music
import webbrowser
import pyautogui
import time
import os
import sys
from PIL import Image
import cv2
import getpass
import numpy as np
import glob


# YOU NEED TO BE LOGGED INTO SHAZAM BFEOREHAND BOTH ON MAC AND IPHONE


def song_separate(path, firstRun):
	x = 1100
	y = 560
	im = Image.open(path)
	pix = im.load()
	while str(pix[x, y]) == str("(90, 202, 250, 255)"):
		y += 1
	startingy = y + 432
	
	img = cv2.imread(path)
	crop_imgs = []
	
	if firstRun:
		crop_imgs.append(img[startingy:startingy + 204, 309:1130])
		crop_imgs.append(img[startingy+204:startingy+408, 309:1130])
		crop_imgs.append(img[startingy+408:startingy+612, 309:1130])
	else:
		crop_imgs.append(img[startingy+612:startingy+816, 309:1130])
	
	for k in crop_imgs:
		if np.array_equal(k[185, 500], np.array([255, 255, 255])):
			im = Image.fromarray(k)
			im_path = '/Users/' + getpass.getuser() + '/Downloads' + '/cropped.png'
			im.save(im_path)
			
			song, artist = ocr.to_txt(im_path)
			files = list()
			for (dirpath, dirnames, filenames) in os.walk('/Users/' + getpass.getuser() + '/Music/iTunes/iTunes Media'):
				files += [os.path.join(dirpath, file) for file in filenames if file[-4:] == '.mp3']
			
			
			
			if song != '' and artist != '':
				url = music.get_url(song, artist)
				mp3_path = music.download(url)
				thumbnail_path = music.get_thumbnail(song, artist)
				music.set_thumbnail(mp3_path, thumbnail_path)
			os.system('say "download complete"')
		else:
			os.system('say "Shortcut Shazam has all downloaded your stupid songs you fucking bitch"')
			sys.exit(1)


def main():
	webpage = webbrowser.open('https://www.shazam.com/myshazam')
	pyautogui.moveTo(1420, 270)
	time.sleep(2.5)
	for i in range(0, 17):
		fullscreen = pyautogui.screenshot('/Users/' + getpass.getuser() + '/Downloads/fullscreen.png')
		
		if i == 0: first_run = True
		else: first_run = False
		
		song_separate('/Users/' + getpass.getuser() + '/Downloads/fullscreen.png', firstRun=first_run)
		
		if i % 2 == 0: pyautogui.scroll(-2)
		else: pyautogui.scroll(-3)
	

if __name__ == '__main__':
	main()
