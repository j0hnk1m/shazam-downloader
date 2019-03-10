#input is image
#
#return song title and artist
###########################################

# import the necessary packages

from PIL import Image
import image
import pytesseract



def to_txt(img_path):
	im = Image.open(img_path)
	text = pytesseract.image_to_string(im, lang = "eng")
	print(text)

print(to_txt("/Users/teddy/Desktop/test4.png"))