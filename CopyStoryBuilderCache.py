#!**--coding:utf8--**

import sys
import os
import shutil
import time


temp_dir = r'C:\Users\newer\AppData\Local\Temp'
cache_n = r'StoryBuilder.dat'
outdir = r'E:\hzw\decode_dab'
cache_f = os.path.join(temp_dir, cache_n)
last_stat = None
#compare_attrs = ( 'st_atime', 'st_atime_ns', 'st_ctime', 'st_ctime_ns', 'st_dev', 'st_file_attributes', 'st_gid', 'st_ino',
#  'st_mode', 'st_mtime', 'st_mtime_ns', 'st_nlink', 'st_reparse_tag', 'st_size', 'st_uid')
compare_attrs = ('st_size', 'st_mtime')


def last_one_diff():
    global last_stat
    result = last_stat is None
    fs = os.stat(cache_f)
    if not result:
        for attr in compare_attrs:
            if getattr(fs, attr) != getattr(last_stat, attr):
                result = True
                break
    if result:
        last_stat = fs
        print("Update last_stat:")
        print(last_stat)
    return result


def copy_a_dat(d, fid):
    target = os.path.join(outdir, d, "%04d.mp3"%fid)
    if last_one_diff():
        shutil.copy(cache_f, target)
        print("copied %s" % target)
        return fid + 1
    return fid

def main_loop(d):
    if not os.path.isdir(outdir):
        os.mkdir(outdir)
    if not os.path.isdir(os.path.join(outdir, d)):
        os.mkdir(os.path.join(outdir, d))
    fid = 1
    while True:
        fid = copy_a_dat(d, fid)
        time.sleep(0.5)


if __name__ == "__main__":
    main_loop(r'SSS')

