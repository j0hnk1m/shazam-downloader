from PIL import Image
import pytesseract


def to_txt(path):
	im = Image.open(path)
	text = pytesseract.image_to_string(im, lang="eng")
	print(text)
	
	song, artist = text.split('\n')
	return song, artist

