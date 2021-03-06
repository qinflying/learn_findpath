#-*- coding:utf-8 -*-
#http://gad.qq.com/article/detail/33637
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

Init()

if __name__ == '__main__':
	import sys
	from colorama import Fore

	s = "1.DFS深度优先搜索.\n"
	s+= "2.BFS广度优先搜索.\n"
	s+= "3.Dijkstra算法.\n"
	s+= "4.A*算法.\n"
	# s+= "5.A*算法 扫地机器人.\n"
	sys.stdout.write(Fore.YELLOW+s)

	c = raw_input("请输入选项:")
	if c == "1":
		import dfsmaze
		dfsmaze.Demo()
	elif c == "2":
		import bfsmaze
		bfsmaze.Demo()
	elif c == "3":
		import dijkstra
		dijkstra.Demo()
	elif c == "4":
		import astar
		astar.MazeDemo()
	elif c == "5":
		import astar
		astar.RobotDemo()
