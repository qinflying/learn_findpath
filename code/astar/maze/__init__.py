#-*- coding:utf-8 -*-
#https://www.cnblogs.com/zhoug2020/p/3468167.html
#https://blog.csdn.net/xgf415/article/details/75200047
#https://blog.csdn.net/zhangxiaofan666/article/details/71715098
# µœ÷À„∑®
#https://blog.csdn.net/zhulichen/article/details/78786493
from . import ui 
import time
import math
MAX_COST = 999999
def Demo():
	oWork = CAStar()
	oWork.work()

class CNode(object):
	def __init__(self, x=0, y=0, cost=9999, f=99999):
		self.m_X = x
		self.m_Y = y 
		self.m_Cost = cost 
		self.m_FValue = f
		self.m_PreviousNode = None 

	def setPreviousNode(self, o):
		self.m_PreviousNode = o 

	def getPreviousNode(self):
		return self.m_PreviousNode

	def getXY(self):
		return self.m_X, self.m_Y 

	def setXY(self, x, y):
		self.m_X = x 
		self.m_Y = y

	def getCost(self):
		return self.m_Cost

	def setCost(self, c):
		self.m_Cost = c

	def getFValue(self):
		return self.m_FValue

	def setFValue(self, f):
		self.m_FValue = f

	def G(self):
		return self.m_Cost + self.m_FValue

class CPriorityQueue(object):
	def __init__(self):
		self.m_Queue = []


	def empty(self):
		return len(self.m_Queue) == 0

	def poll(self):
		o = self.m_Queue.pop(0)
		return o 

	def push(self, o):
		index = len(self.m_Queue)
		for idx, e in enumerate(self.m_Queue):
			if e.G() > o.G():
				index = idx 
				break 

		self.m_Queue.insert(index, o)

class CAStar(object):
	def __init__(self):
		self.m_Queue = CPriorityQueue() 
		self.m_Map = ui.CMap()
		self.m_CloseList = []

	def Reset(self):
		self.m_Queue = CPriorityQueue() 
		self.m_Map = ui.CMap()
		self.m_CloseList = []

	def work(self):
		self.Reset()
		self.m_Map.Print()

		x, y = self.m_Map.GetHero()
		ex, ey = self.m_Map.GetEnd()
		f = self.calF((x, y), (ex, ey))
		oInitNode = CNode(x, y, 0, f)

		self.m_Queue.push(oInitNode)

		while not self.m_Queue.empty():
			oNode = self.m_Queue.poll()

			x, y = oNode.getXY()

			if x == ex and y == ey:
				self.output(oNode)
				break

			for dx, dy in d_defines.EIGHT_DIRS:
				tx = x + dx
				ty = y + dy

				#‰∏çÂèØËæ?
				if not self.m_Map.IsCantainer(tx, ty) or self.m_Map.IsChar(tx, ty, d_defines.TYPE_WALL):
					continue

				cost = oNode.getCost() + self.calCost((x, y), (tx, ty))
				f = self.calF((tx, ty), (ex, ey))
				oNewNode = CNode(tx, ty, cost, f)
				oNewNode.setPreviousNode(oNode)

				if not self.isInVisited(tx, ty):
					self.m_Queue.push(oNewNode)
					self.m_CloseList.append((tx, ty))
					self.m_Map.Print(self.m_CloseList)
					time.sleep(0.1)

	def calCost(self, current, next):
		cx, cy = current
		nx, ny = next

		#water‰ºöÂ¢ûÂä?1‰∏™ÁÇπÁöÑÊ∂àËÄ?
		if self.m_Map.IsChar(nx, ny, d_defines.TYPE_WATER):
			watercost = 1
		else:
			watercost = 0

		cost = watercost + math.sqrt((cx - nx) * (cx - nx) + (cy - ny) * (cy - ny))
		return cost

	def calF(self, current, end):
		cx, cy = current
		ex, ey = end

		return abs(cx - ex) + abs(cy - ey)

	def output(self, oNode):
		lst = []
		while oNode:
			lst.append(oNode.getXY())
			oNode = oNode.getPreviousNode()

		lst = lst[-1::-1]
		self.m_Map.PrintWithPath(lst)

	def isInVisited(self, x, y):
		return (x, y) in self.m_CloseList






