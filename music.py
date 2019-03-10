from __future__ import unicode_literals
import os
import urllib
import requests
import re
import youtube_dl
import getpass
from google_images_download import google_images_download
from PIL import Image
import eyed3


def get_url(song, artist):
	query = urllib.parse.quote(song + ' ' + artist + ' lyrics')
	response = requests.get('https://www.youtube.com/results?search_query=' + query).text
	p = re.findall(r'\/watch\?v=([^:]+?)"', response)[0]
	url = 'https://www.youtube.com/watch?v=' + p
	print(url)
	return url


def download(url):
	pwd = os.getcwd()
	dir = '/Users/' + getpass.getuser() + '/Downloads/ss_downloads/'
	if not os.path.exists(dir):
		os.makedirs(dir)
	
	os.chdir(dir)
	ydl_opts = {'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio',
																'preferredcodec': 'mp3', 'preferredquality': '192'}]}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		info = ydl.extract_info(url, download=True)
		filename = ydl.prepare_filename(info)[:-5] + '.mp3'
	
	os.chdir(pwd)
	return dir + filename


def get_thumbnail(song, artist):
	query = song + " " + artist
	response = google_images_download.googleimagesdownload()
	args = {'keywords': query, 'suffix_keywords': "album cover art", 'limit': 2, 'print_urls': True}
	pwd = os.getcwd()
	os.chdir('/Users/' + getpass.getuser() + '/Downloads')
	img_paths = response.download(args)
	
	for k, v in img_paths.items():
		v1 = Image.open(v[0])
		v2 = Image.open(v[1])
		
		if v1.size[0] > v2.size[0]:
			thumbnail = v[0]
		else:
			thumbnail = v[1]
	
	os.chdir(pwd)
	return thumbnail


def set_thumbnail(mp3, thumbnail):
	f = eyed3.load(mp3)
	if f.tag is None:
		f.initTag()
	
	f.tag.images.set(3, open(thumbnail, 'rb').read(), 'image/jpeg')
	f.tag.save()
