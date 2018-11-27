#-*- coding:utf-8 -*-
from colorama import Fore, Back
WALL_C = "■"
HERO_C = "★"
END_C = "●"
EMPTY = "  "
PATH_C = "◆"

C2COLOR = {
	WALL_C : Fore.YELLOW,
	EMPTY :	Back.WHITE,
	HERO_C : Fore.GREEN,
	END_C : Fore.GREEN,
	PATH_C : Fore.RED
}

#四方位
FOUR_DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


