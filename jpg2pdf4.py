#-*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image as image
from PIL import ImageDraw, ImageFont
import numpy as np
import functools
import time


def check_contain_chinese(check_str):
  for ch in check_str.decode('utf-8'):
    if u'\u4e00' <= ch <= u'\u9fff':
      return True
  return False


def concat_pdf(f_pdf, lines, col=3, row=17):
  (h4, w4) = landscape(A4)
  pages = col * row
  margin = 25
  header_h = 20
  header_font_size = 20
  h_offset = 5
  w_offset = 0
  h = h4 - header_h - 2 * margin
  w = w4 - 2 * margin
  ha = (h - (row - 1) * h_offset) / row
  wa = (w - (col - 1) * w_offset) / col
  h_col = [margin*1 + x *(ha + h_offset) for x in range(row)]
  w_row = [margin*1 + x *(wa + w_offset) for x in range(col)]
  dt = np.dtype([('x', float), ('y', float)])
  pos = np.empty([pages], dtype=dt)
  for i1 in range(pages):
    hi = row - i1//col - 1
    wi = i1 % col
    pos[i1] = (w_row[wi], h_col[hi])
  print(pos)
  #return
  c = canvas.Canvas(f_pdf, pagesize = (w4, h4))
  i = 0
  for line in lines:
    line = line.strip()
    if i % pages  == 0 :
      header_txt = header_prefix % (i//pages +1)
      c.setFont('huaWenXingKai', header_font_size)
      c.setFillColorRGB(0, 0xcc, 0xcc)
      c.drawCentredString(w4/2, h + margin + 5, header_txt)
    print("[%s][%s]"%(i+1, line))
    c.drawImage(jpg_f, pos[i%pages]['x'], pos[i%pages]['y'], wa, ha)
    #c.setStrokeColorRGB(255,0,0)
    if check_contain_chinese(line):
      c.setFont('huaWenXingKai', 16)
    else:
      c.setFont('timesNewRoman', 16)
    #if i % 2 == 0:
    #  c.setFillColorRGB(0, 0, 0)
    #else:
    c.setFillColorRGB(128, 0, 128)
    c.drawCentredString(pos[i%pages]['x'] + wa/2, pos[i%pages]['y'] + ha/2 - 5, line)
    if i % pages  == pages -1 :
      c.showPage()
    i += 1
  c.save()

  
n_1_page = 51
res_dir = 'resources'
jpg_f = os.path.join(res_dir, '1.jpeg')
header_prefix = u"贝乐虎儿歌%s"
input_file = u'D:\private\hd\son\贝乐虎儿歌\list.txt'
out_name = os.path.basename(os.path.splitext(input_file)[0])


if __name__ == "__main__":
    pdfmetrics.registerFont(TTFont('huaWenXingKai', r'C:\Windows\Fonts\STXINGKA.TTF'))
    pdfmetrics.registerFont(TTFont('timesNewRoman', r'C:\Windows\Fonts\times.ttf'))
    with open(input_file, 'rb') as fi:
        lines = [x.strip() for x in fi]
    output = "result_%s_%s.pdf" % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), os.getpid())
    concat_pdf(output, lines)
    print("The file %s generated successfully!\n" % output)
  