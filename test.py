from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sys

def copyright_apply(input_image_path,
                   output_image_path,
                   text):
    photo = Image.open(input_image_path)
    
    #Store image width and height
    w, h = photo.size
    
    # make the image editable
    drawing = ImageDraw.Draw(photo)
    font = ImageFont.truetype("arial.ttf", 20)
    
    #get text width and height
    text = "©️ " + text + "   "
    text_w, text_h = drawing.textsize(text, font)
    pos = w - text_w - 450, (h - text_h) - 550
    drawing.text(pos, text, fill="#B7FF33", font=font)
    photo.save(output_image_path)
    
copyright_apply(sys.argv[1],'ow.jpeg', 'Manavalan Micheal')
