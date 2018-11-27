#-*- coding:utf-8 -*-
def ReLoadCode():
	import sys
	import codecs
	sys.stdout = codecs.EncodedFile(sys.stdout, 'utf-8', 'gbk')

def ColoramaInit():
	import colorama
	colorama.init(autoreset=True)

def Init():
	ReLoadCode()
	ColoramaInit()

if __name__ == '__main__':
	Init()
	import dfsmaze
	dfsmaze.Demo()
