# -*- coding: utf-8 -*-
# !/usr/bin/env python

import os
import chardet


n_1_page = 51
res_dir = 'resources'
template_f = os.path.join(res_dir, 'rec_template.htm')
header_f = os.path.join(res_dir, 'rec_header.html')
input_file = u'D:\\pycharmProject\\TalkyPen\\resources\\贝乐虎儿歌.txt'
out_html = '%s_%s.html'
out_name = os.path.basename(os.path.splitext(input_file)[0])

def gen_a_pdf(n):
    outs = []
    out_str = header_str
    outs.append(out_str)
    for line in lines[n* n_1_page: min(len(lines), (n+1) * n_1_page)]:
        line = line.strip()
        out_str = template_str % line
        outs.append(out_str.decode('utf8').encode('gbk'))
    outs.append(b'''</div>
    </body>
    </html>'''
    )
    out_f = out_html % (out_name, n)
    with open(out_f, 'wb') as fo:
        fo.write(b''.join(outs))


if __name__ == "__main__":
    with open(header_f, 'rb') as fh:
        header_str = fh.read()
    with open(template_f, 'rb') as ft:
        template_str = ft.read()
    with open(input_file, 'rb') as fi:
        lines = [x.strip() for x in fi]
    for ns in range((len(lines)-1)//n_1_page + 1):
        gen_a_pdf(ns)