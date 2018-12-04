#-*- coding:utf-8 -*-
#解救小哈：https://www.cnblogs.com/OctoptusLian/p/7429645.html
#非常暴力
import defines
import time

def DFS(oMapHandler, x, y, step, stack):
	#终点位置
	if oMapHandler.IsChar(x, y, defines.END_C):
		if oMapHandler.GetMiniStep() > step:
			oMapHandler.SetMiniStep(step)
			oMapHandler.SetPaths(stack)
		return step

	#四周位置
	for dx, dy in defines.FOUR_DIRS:
		tx = x + dx 
		ty = y + dy 
		#不可达位置
		if not oMapHandler.IsCantainer(tx, ty) or oMapHandler.IsChar(tx, ty, defines.WALL_C):
			continue

		#回到起点
		if oMapHandler.IsChar(tx, ty, defines.HERO_C):
			continue

		#已经到达的地点
		if oMapHandler.GetBook(tx, ty):
			continue

		stack.append((tx, ty))
		oMapHandler.Print()

		oMapHandler.SetBook(tx, ty, 1)
		tp = DFS(oMapHandler, tx, ty, step+1, stack)
		if tp:
			return tp
		if stack:
			stack.pop()
		oMapHandler.SetBook(tx, ty, 0)		
	return 0


def Demo():
	import ui 
	oMap = ui.CMap()
	oMap.Print()

	oMap.ClearDFS()
	x, y = oMap.m_Hero
	stack = []
	DFS(oMap, x, y, 0, stack)

	oMap.PrintWithPath()





