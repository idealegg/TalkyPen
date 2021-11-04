# -*- coding: utf-8 -*-
# !/usr/bin/env python

import os
import re
import shutil


#check_dir = r'D:\private\hd\son\hht\儿歌'
check_dir = r'D:\private\hd\son\hht\故事'
os.chdir(check_dir)
if 1:
    fs = os.listdir('.')
    for f in fs:
        try:
            os.rename(f, re.sub('^[0-9 .]+', '', f))
        except Exception as e:
            os.unlink(f)
os.mkdir('mp3')
os.mkdir('mp3_2')
fs = os.listdir('.')
l = []
for f in fs:
    l.append(f.replace('.mp3', ''))
    shutil.move(f, 'mp3')