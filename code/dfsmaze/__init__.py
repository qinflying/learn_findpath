#-*- coding:utf-8 -*-
#解救小哈：https://www.cnblogs.com/OctoptusLian/p/7429645.html
import defines
import time

def DFS(oMapHandler, x, y, step, stack):
	#不可达位置
	if not oMapHandler.IsCantainer(x, y) or oMapHandler.IsChar(x, y, defines.WALL_C):
		return 0
	#终点位置
	if oMapHandler.IsChar(x, y, defines.END_C):
		return step

	#stack.append((x, y))

	#四周位置
	for dx, dy in defines.FOUR_DIRS:
		tx = x + dx 
		ty = y + dy 
		#不可达位置
		if not oMapHandler.IsCantainer(tx, ty) or oMapHandler.IsChar(tx, ty, defines.WALL_C):
			continue

		if (tx, ty) in stack:
			continue

		#终点位置
		if oMapHandler.IsChar(tx, ty, defines.END_C):
			return step

		oMapHandler.SetBook(tx, ty, 1)
		oMapHandler.Print()
		time.sleep(0.5)
		r = DFS(oMapHandler, tx, ty, step+1, stack)
		oMapHandler.SetBook(tx, ty, 0)		
		if r:
			return r
	return 0


def Demo():
	import ui 
	oMap = ui.CMap()
	oMap.Print()

	oMap.ClearBooks()
	x, y = oMap.m_Hero
	stack = []
	step = DFS(oMap, x, y, 0, stack)

	print step, stack





