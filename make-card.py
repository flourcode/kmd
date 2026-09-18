#!/usr/bin/env python3
"""Regenerate card.jpg (1200x630 OpenGraph image) in the site's own palette and typeface.
Run from the web-root folder. Needs: pillow, fonttools, brotli.
Inter is extracted from index.html's embedded @font-face so the card can never drift from the page."""
import re, base64, io, os
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

HEADLINE = ['Before you put it in commit,', 'try to kill it.']
DEK      = 'Five questions to separate proof from hopium before your manager does.'
FOOT     = 'Built for federal sellers. No login. No CRM.'
URL      = 'killmydeal.com'
PILLARS  = ['CUSTOMER', 'MONEY', 'POWER', 'PATH', 'NOW']

W, H, M = 1200, 630, 72
SURF=(0xF7,0xFA,0xFF); INK=(0x18,0x1C,0x20); VAR=(0x41,0x47,0x4E); PINK=(0x04,0x55,0x95)
PRIMC=(0xCD,0xE8,0xFE); ONPRIMC=(0x01,0x1C,0x32)

html = open('index.html').read()
woff2 = base64.b64decode(re.search(r'font/woff2;base64,([A-Za-z0-9+/=]+)\)', html).group(1))
def font(w, size):
    inst = instancer.instantiateVariableFont(TTFont(io.BytesIO(woff2)), {'wght': w}, inplace=False)
    inst.flavor = None; buf = io.BytesIO(); inst.save(buf); buf.seek(0)
    return ImageFont.truetype(buf, size)

im = Image.new('RGB', (W, H), SURF); d = ImageDraw.Draw(im)
bird = Image.open('bluebird.png').convert('RGBA')
bh = 52; bw = int(bird.width * bh / bird.height); bird = bird.resize((bw, bh), Image.LANCZOS)
im.paste(bird, (M, M - 4), bird)
d.text((M + bw + 18, M + 2), 'KILL MY DEAL', font=font(700, 30), fill=INK)
hf = font(800, 74); y = M + 104
for line in HEADLINE:
    d.text((M - 3, y), line, font=hf, fill=INK); y += 88
d.text((M, y + 14), DEK, font=font(400, 29), fill=VAR)
cy = y + 84; cx = M; cf = font(700, 25)
for t in PILLARS:
    pw = int(d.textlength(t, font=cf) + 52)
    d.rounded_rectangle((cx, cy, cx + pw, cy + 54), radius=14, fill=PRIMC)
    d.text((cx + 26, cy + 13), t, font=cf, fill=ONPRIMC); cx += pw + 16
fy = H - M - 20
d.text((M, fy), FOOT, font=font(400, 24), fill=VAR)
uf = font(700, 26)
d.text((W - M - d.textlength(URL, font=uf), fy - 2), URL, font=uf, fill=PINK)
im.save('card.jpg', quality=90, optimize=True)
print('card.jpg', os.path.getsize('card.jpg'), 'bytes')
