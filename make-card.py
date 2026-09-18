#!/usr/bin/env python3
"""Regenerate the 1200x630 OpenGraph cards in the site's own palette and typeface.
  python3 make-card.py deal       -> card.jpg
  python3 make-card.py pipeline   -> card-pipeline.jpg
Run from the web-root folder. Needs: pillow, fonttools, brotli. Uses inter.woff2 so the cards cannot drift from the pages."""
import re, base64, io, os
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

import sys
CARDS = {
  'deal': dict(out='card.jpg', wordmark='KILL MY DEAL',
    headline=['Before you put it in commit,', 'try to kill it.'],
    dek='Five questions to separate proof from hopium before your manager does.',
    foot='Built for federal sellers. No login. No CRM.', url='killmydeal.com',
    pillars=['CUSTOMER', 'MONEY', 'POWER', 'PATH', 'NOW']),
  'pipeline': dict(out='card-pipeline.jpg', wordmark='KILL MY PIPELINE',
    headline=['3X is a rule of thumb.', 'Your win rate may disagree.'],
    dek='Coverage against your target and your own conversion, not a benchmark.',
    foot='For sales managers. No login. Nothing stored.', url='killmydeal.com/pipeline',
    pillars=['TARGET', 'COVERAGE', 'WIN RATE']),
}
C = CARDS[sys.argv[1] if len(sys.argv) > 1 else 'deal']
HEADLINE, DEK, FOOT, URL, PILLARS = C['headline'], C['dek'], C['foot'], C['url'], C['pillars']

W, H, M = 1200, 630, 72
SURF=(0xFF,0xFF,0xFF); INK=(0x1D,0x1D,0x1F); VAR=(0x6E,0x6E,0x73); PINK=(0x1D,0xA1,0xF2)
PRIMC=(0xF5,0xF5,0xF7); ONPRIMC=(0x1D,0x1D,0x1F)

woff2 = open('inter.woff2', 'rb').read()
def font(w, size):
    inst = instancer.instantiateVariableFont(TTFont(io.BytesIO(woff2)), {'wght': w}, inplace=False)
    inst.flavor = None; buf = io.BytesIO(); inst.save(buf); buf.seek(0)
    return ImageFont.truetype(buf, size)

im = Image.new('RGB', (W, H), SURF); d = ImageDraw.Draw(im)
bird = Image.open('bluebird.png').convert('RGBA')
bh = 52; bw = int(bird.width * bh / bird.height); bird = bird.resize((bw, bh), Image.LANCZOS)
im.paste(bird, (M, M - 4), bird)
d.text((M + bw + 18, M + 2), C['wordmark'], font=font(700, 30), fill=INK)
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
im.save(C['out'], quality=90, optimize=True)
print(C['out'], os.path.getsize(C['out']), 'bytes')
