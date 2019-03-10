from __future__ import unicode_literals
import os
import sys
import urllib
import requests
import re
import youtube_dl
import getpass


def get_url(song, artist, lyrics):
	if lyrics:
		query = urllib.parse.quote(song + ' ' + artist)
	else:
		query = urllib.parse.quote(song + ' ' + artist + ' lyrics')
	response = requests.get('https://www.youtube.com/results?search_query=' + query).text
	p = re.findall(r'\/watch\?v=([^:]+?)"', response)[0]
	url = 'https://www.youtube.com/watch?v=' + p
	print(url)
	return url


def download(url):
	user = getpass.getuser()
	os.chdir('/Users/' + user + '/Music/iTunes/iTunes Media/Automatically Add to iTunes.localized')
	ydl_opts = {'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio',
															'preferredcodec': 'mp3', 'preferredquality': '192'}]}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])
