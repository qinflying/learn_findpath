#-*- coding:utf-8 -*-
from colorama import Fore, Back
TYPE_EMPTY = 0 		#空
TYPE_WALL = 1		#墙
TYPE_PATH = 7 		#路径
TYPE_ROBOT = 8		#机器人
TYPE_DIRTY = 9 		#灰尘

I2CHAR = {
	TYPE_EMPTY : "  ",
	TYPE_WALL : "■",
	TYPE_ROBOT : "★",
	TYPE_DIRTY : "●",
	TYPE_PATH : "◆",
}

#前景颜色
I2FCOLOR = {
	TYPE_WALL : Fore.YELLOW,
	TYPE_EMPTY :	Back.WHITE,
	TYPE_ROBOT : Fore.GREEN,
	TYPE_DIRTY : Fore.GREEN,
	TYPE_PATH : Fore.RED,
}

#背景颜色
I2BCOLOR = {
	
}

#四方位
FOUR_DIRS = [
	(-1, 0),
	(0, -1),
	(1, 0),
	(0, 1),
]