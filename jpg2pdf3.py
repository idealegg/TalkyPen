#-*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from PIL import Image as image
from PIL import ImageDraw, ImageFont
import numpy as np
import functools
import time


def cmp(a,b):
  if a<b:
    return -1
  elif a>b:
    return  1
  else:
    return 0


def draw_header(text, fillColor = "#00cccc", out='out.png', size=40, ttf=r'C:\Windows\Fonts\STXINGKA.TTF'):
  #ttf=r'C:\Windows\Fonts\STXINGKA.TTF'  #华文行楷
  setFont = ImageFont.truetype(ttf, size)
  text_len=size*len(text)
  #生成大小为400x400RGBA是四通道图像，RGB表示R，G，B三通道，A表示Alpha的色彩空間
  im = image.new(mode='RGB', size=(text_len, size), color=(255, 255, 255))
  # ImageDraw.Draw 简单平面绘图
  draw = ImageDraw.Draw(im=im)
  draw.text((0,0),text,font=setFont,fill=(0,0xcc,0xcc),direction=None)
  #im = im.resize(text_len, size, 0)
  #im.save(out, format="jpeg", quality=95, optimize=True)
  #im = im.convert('RGB')
  im.save(out)
  im.close()
  return text_len, size

def comp(x,y):
  i = cmp(len(x),len(y))
  return i if i else cmp(x,y)

def comp2(x,y):
  xs = x.split('_')
  ys = y.split('_')
  for i in range(len(xs)):
    j = comp(xs[i], ys[i])
    if j:
      return j
  return comp(x, y)


def get_file_list(dir):
  #if sys.version[0] == 3:
  return map(lambda x: os.path.join(dir, x), sorted(os.listdir(dir), key=functools.cmp_to_key(comp2)))
  #else:
  #return map(lambda x: os.path.join(dir, x),   sorted(os.listdir(dir), comp2))


def concat_pdf(f_pdf, f_list, num = 3):
  (h4, w4) = landscape(A4)
  pages = num ** 2
  margin = 25
  header_h = h4/10/num
  offset = w4/20/num
  h = h4 - header_h - 2 * margin
  w = w4 - 2 * margin
  ha = (h - (num - 1) * offset) / num
  wa = (w - (num - 1) * offset) / num
  h_col = [margin*1 + x *(ha + offset) for x in range(num)]
  w_row = [margin*1 + x *(wa + offset) for x in range(num)]
  dt = np.dtype([('x', float), ('y', float)])
  pos = np.empty([pages], dtype=dt)
  for i1 in range(pages):
    hi = num - i1//num - 1
    wi = i1 % num
    pos[i1] = (w_row[wi], h_col[hi])
  print(pos)
  #return
  c = canvas.Canvas(f_pdf, pagesize = (w4, h4))
  i = 0
  for jpg in f_list:
    if i % pages  == 0 :
      header_txt = u"古诗词%s" % (i//pages +1)
      header_f = 'header%s.jpeg' % (i//pages +1)
      print(header_txt)
      hw, hh = draw_header(header_txt, out=header_f)
      header_w = header_h * hw / hh
      c.drawImage(header_f, w4/2 - header_w/2, h + margin, header_w, header_h)
      os.remove(header_f)
    print("[%s][%s]"%(i+1, jpg))
    c.drawImage(jpg, pos[i%pages]['x'], pos[i%pages]['y'], wa, ha)
    if i % pages  == pages -1 :
      c.showPage()
    i += 1
  c.save()

  
if __name__ == "__main__":
  if 1:
    input_dir = r'D:\BaiduNetdiskDownload\宝宝巴士古诗大字图\jpgs'
  else:
    if len(sys.argv) != 2 or not os.path.isdir(sys.argv[1]) :
      print ("Usage: %s <jpgs_dir>\n" % os.path.basename(sys.argv[0]))
      print ("       <jpgs_dir> : the directory path of jpg files\n")
      exit(1)
      input_dir = sys.argv[1]
  output = "result_%s_%s.pdf" % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), os.getpid())
  concat_pdf(output, get_file_list(input_dir), 4)
  print ("The file %s generated successfully!\n" % output)
  