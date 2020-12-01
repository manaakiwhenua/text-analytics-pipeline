# first test of using ocr on pdfs with python

# dependencies:
# tesseract

from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io
import codecs
import os

tool = pyocr.get_available_tools()[0]
req_image = []
final_text = []

f = io.open("PDFs/greenslade2018.txt", encoding='utf-8', mode='w')

image_pdf = Image(filename="PDFs/greenslade2018.pdf", resolution=600)
image_jpeg = image_pdf.convert('jpeg')

# wand converted each page in the PDF into its own image blob
# loop over them and append them as a blob into the req_image list

for img in image_jpeg.sequence:
	img_page = Image(image=img)
	req_image.append(img_page.make_blob('jpeg'))

# ocr over image blobs
for img in req_image:
	txt = tool.image_to_string(
			PI.open(io.BytesIO(img)),
			#lang=lang,
			builder=pyocr.builders.TextBuilder()
		)
	final_text.append(txt.encode('utf-8', 'ignore'))
    #final_text.append(txt)

for item in final_text:
	f.write(u"%r" % item)
f.close()

#delete image magick temp files
DITF = 'rm /tmp/magick*'
#check they are deleted
ls = 'ls /tmp/'
os.system(DITF)
os.system(ls)
