# -*- coding: utf-8 -*-

# python生成sitemap，超过5万条数据自动生成新文件。
# from __future__ import division
# date:2016-3-18

# Author:赵彦刚@zhaoyangang.cn

import os, datetime

# import sys

# reload(sys)

# sys.setdefaultencoding('utf-8')
# 手动设置你网站的域名，别忘记了结尾的斜杠!
host = 'http://m.v.baidu.com/'

# 自动新建一个存放sitemap.xml的文件夹，默认叫sitemap，可自行修改。
dir = os.popen('mkdir static')
# dir = os.mkdir('sitemap')

# 设定sitemap.xml文件存放的路径，别忘记了结尾的斜杠!
path = 'static/'

lastmod = datetime.date.today()

def add_file(j, f1, host, path):
    file_name = 'watch_sitemap_%s.xml'%(j)
    f1.write("  <sitemap>\n    <loc>%s%s%s</loc>\n    <lastmod>%s</lastmod>\n  </sitemap>\n"%(host, path, file_name, lastmod))
    # a追加模式写入
    f = open("%s%s"%(path, file_name), "a")
    f.write('<?xml version="1.0" encoding="utf-8"?>\n')
    f.write('<urlset>\n')
    return f

# 判断总的URL数
c = 0

for i in open('urls.txt'):
    url = i.strip()
    if len(url) == 0:
        pass
    else:
        c+=1

# 判断需要生成的sitemap个数
file_num = c%50000

if file_num == 0:
    file_num = c/50000
    print ('总共有%s条URL, 生成%s个sitemap个文件' % (c, file_num))
else:
    file_num = (c/50000)+1
    print ('总共有%s条URL, 生成%s个sitemap文件' % (c, file_num))

# 自动按5W条URL生成sitemap，并自动命名为sitemap_1.xml
i = 0
j = 2
# https://docs.python.org/3/library/functions.html#open
f = open('%s/watch_sitemap_1.xml'%(path), 'w+')
f.write('<?xml version="1.0" encoding="utf-8"?>\n')
f.write('<urlset>\n')
# a追加模式写入
f1 = open('%s/watch_sitemapindex.xml'%(path), 'a')
f1.write('<?xml version="1.0" encoding="utf-8"?>\n')
f1.write('<sitemapindex>\n')
f1.write("  <sitemap>\n    <loc>%s%s%s</loc>\n    <lastmod>%s</lastmod>\n  </sitemap>\n"%(host, path, 'sitemap_1.xml', lastmod))

for url in open("urls.txt"):
    url = url.strip()
    i += 1
    if i == 50000 or j == 50000:
        f.write('</urlset>')
        f.close()
        i = 0
        f = add_file(j, f1, host, path)
        j += 1
    f.write("  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>0.8</priority>\n  </url>\n"%(url, lastmod))

f1.write('</sitemapindex>')
f1.close()
