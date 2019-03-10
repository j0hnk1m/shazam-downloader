#input is image
#
#return song title and artist
###########################################

# import the necessary packages

from PIL import Image
import image
import pytesseract

im = Image.open("/Users/teddy/Desktop/words1.png")

text = pytesseract.image_to_string(im, lang = "eng")

print(text)