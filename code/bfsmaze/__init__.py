#-*- coding:utf-8 -*-
#https://www.cnblogs.com/Goden/p/3962131.html
import defines
import time

#四方位
FOUR_DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def BFS(oMapHander, x, y):
	queue = []
	queue.append((x, y))

	oMapHander.SetBook(x, y, 1)
	bEnd = False
	while queue:
		x, y = queue.pop(0)
		for dx, dy in FOUR_DIRS:
			tx = x + dx 
			ty = y + dy

			#不可达
			if not oMapHander.IsCantainer(tx, ty) or oMapHander.IsChar(tx, ty, defines.WALL_C):
				continue

			#已到达点
			if oMapHander.GetBook(tx, ty):
				continue

			if oMapHander.IsChar(tx, ty, defines.END_C):
				bEnd = True 
				break

			queue.append((tx, ty))
			oMapHander.SetBook(tx, ty, 1)
			oMapHander.Print()
			time.sleep(0.1)
			oMapHander.SetPaths(tx, ty, x, y)

		if bEnd:
			break


def Demo():
	import ui 
	oMap = ui.CMap()
	oMap.Print()

	oMap.ClearBFS()
	x, y = oMap.m_Hero
	BFS(oMap, x, y)
	oMap.PrintWithPath()





