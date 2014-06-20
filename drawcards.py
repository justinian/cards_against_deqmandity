import Image
import ImageDraw
import ImageFont
import textwrap

heart = Image.open("heart.png").convert("L")
text_font = ImageFont.truetype("open-sans/OpenSans-Bold.ttf", 62)
attr_font = ImageFont.truetype("open-sans/OpenSans-Regular.ttf", 40)
black = (0,0,0)
white = (255,255,255)

def draw_card( outfile, card_text, attribution, bg=black, fg=white ):
    image = Image.new("RGBA", (822,1122), bg)
    draw = ImageDraw.Draw(image)

    x = 85
    y = 130
    for line in textwrap.wrap(card_text, 19):
        draw.text((x,y), line, fg, font=text_font)
        y += 85

    w, h = draw.textsize(attribution, font=attr_font)
    draw.text((725-w,995), attribution, fg, font=attr_font)
    image.paste(fg, (725-w-53, 1008), heart)

    image.save(outfile)

import os
import shutil
shutil.rmtree("cards", ignore_errors=True)
os.makedirs("cards/black")
os.makedirs("cards/white")

import csv
import sys
with open('blacks.csv', 'rb') as csvfile:
    i = 0
    for row in csv.reader(csvfile):
        if i > 0:
            text = row[3].decode('utf8').strip()
            if len(text) < 1: continue
            attrib = row[1].decode('utf8').strip()
            draw_card( "cards/black/%d.png" % (i,), text, attrib, bg=black, fg=white )
            sys.stdout.write('.')
            sys.stdout.flush()
        i += 1
    print

with open('whites.csv', 'rb') as csvfile:
    i = 0
    for row in csv.reader(csvfile):
        if i > 0:
            text = row[3].decode('utf8').strip()
            if len(text) < 1: continue
            attrib = row[1].decode('utf8').strip()
            draw_card( "cards/white/%d.png" % (i,), text, attrib, bg=white, fg=black )
            sys.stdout.write('.')
            sys.stdout.flush()
        i += 1
    print

