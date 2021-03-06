#-*- coding:utf-8 -*-
from colorama import Fore, Back
TYPE_EMPTY = 0 		#空
TYPE_WALL = 1		#墙
TYPE_WATER = 6		#水
TYPE_PATH = 7 		#路径
TYPE_HERO = 8		#角色
TYPE_END = 9 		#终点

I2CHAR = {
	TYPE_EMPTY : "  ",
	TYPE_WALL : "■",
	TYPE_HERO : "★",
	TYPE_WATER : "  ",
	TYPE_END : "●",
	TYPE_PATH : "◆",
}

#前景颜色
I2FCOLOR = {
	TYPE_WALL : Fore.YELLOW,
	TYPE_WATER : Back.CYAN,
	TYPE_EMPTY : Back.WHITE,
	TYPE_HERO : Fore.GREEN,
	TYPE_END : Fore.GREEN,
	TYPE_PATH : Fore.RED,
}

#背景颜色
I2BCOLOR = {
	
}

#四方位
EIGHT_DIRS = [
	(-1, 0),
	(-1, -1),
	(0, -1),
	(1, -1),
	(1, 0),
	(1, 1),
	(0, 1),
	(-1, 1),
]