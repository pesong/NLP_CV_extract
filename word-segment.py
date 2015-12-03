# -*- coding: utf-8 -*-

import jieba
import sys
# define file name
profile_name = sys.argv[1]
profile_ext_name = sys.argv[2]
print profile_name, profile_ext_name


profile = open(profile_name)
profile_extract = open(profile_ext_name, 'r+')
line = profile.readline()

while line:
    seg_list = jieba.cut(line, cut_all=False)
    seg_utf = "/ ".join(seg_list).encode('utf-8')
    profile_extract.write(seg_utf)
    line = profile.readline()


profile.close()
profile_extract.close()

pass
