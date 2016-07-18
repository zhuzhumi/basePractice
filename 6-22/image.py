#coding:utf-8

'这是一个图片测试'

__author__ = 'Joan'

from PIL import Image
# import  sys
# a = sys.path
# print a
im = Image.open('D://tree-node.png')
print (im.format,im.size,im.mode)

