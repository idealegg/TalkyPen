#!--**coding:utf8--**
import os
import sys
import pprint
import shutil


outdir = r'D:\BaiduNetdiskDownload\宝宝巴士古诗大字图\output'
lfile = r'D:\BaiduNetdiskDownload\宝宝巴士古诗大字图\list_uniq'
dirs = [
        #r'E:\hzw\xmly\奇妙古诗词---宝宝巴士国学',
        r'E:\hzw\xmly\宝宝巴士·国学儿歌---唐诗三百首',
        ]

lists = [os.listdir(x) for x in dirs]
songs = []
with open(lfile, 'r') as fd:
	songs = [x.strip() for x in fd if x.strip()]
songs2 = {}
for x in songs:
	if x in songs2:
		songs2[x] += 1
	else:
		songs2[x] = 1
#map(lambda x: songs2[x]+=1, songs)
print("songs: %s, songs2: %s" % (len(songs), len(songs2)))
songs3 = list(filter(lambda x: songs2[x]!=1, songs2))
pprint.pprint(songs3)

in_num = {}
not_in = [[], []]
for i1, s in enumerate(songs):
	for i2, l in enumerate(lists):
		r = list(filter(lambda x: x.count(s), l))
		#print("[%s][%s][%s][%s][%s]"%(i1+1, s, 'dir%s'%i2, len(r), r))
		if len(r):
			if dirs[i2] in in_num:
				in_num[dirs[i2]] += 1
			else:
				in_num[dirs[i2]] = 0
			shutil.copy(os.path.join(dirs[i2], r[0]), os.path.join(outdir, "%s_%s"%(i1, r[0])))
		else:
			not_in[i2].append(s)
		if len(r) > 1:
			print("[%s][%s][%s][%s][%s]"%(i1+1, s, 'dir%s'%i2, len(r), r))

#pprint.pprint(in_num)
#pprint.pprint(not_in)
