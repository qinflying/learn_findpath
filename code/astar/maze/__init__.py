#-*- coding:utf-8 -*-
#https://www.cnblogs.com/zhoug2020/p/3468167.html
#https://blog.csdn.net/xgf415/article/details/75200047
#https://blog.csdn.net/zhangxiaofan666/article/details/71715098

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
			if e.G() >= o.G():
				index = idx 
				break 

		self.m_Queue.insert(index, o)

		# print "push:", o.getXY()
		# print "queue:", [(oo.getXY(), int(oo.G())) for oo in self.m_Queue]

	def containerNode(self, o):
		for oo in self.m_Queue:
			if oo.getXY() == o.getXY():
				return oo 
		return None 

	def update(self, o):
		if o in self.m_Queue:
			self.m_Queue.remove(o)
		self.push(o)

class CCloseQueue(object):
	def __init__(self):
		self.m_Queue = []
		self.m_XY = []

	def push(self, o):
		self.m_Queue.append(o)
		self.m_XY.append(o.getXY())

	def container(self, o):
		return o.getXY() in self.m_XY

class CAStar(object):
	def __init__(self):
		self.m_OpenQueue = CPriorityQueue() 
		self.m_Map = ui.CMap()
		self.m_CloseQueue = CCloseQueue()

	def Reset(self):
		self.m_OpenQueue = CPriorityQueue() 
		self.m_Map = ui.CMap()
		self.m_CloseQueue = CCloseQueue()

	def work(self):
		self.Reset()
		self.m_Map.Print()

		lPrint = []

		x, y = self.m_Map.GetHero()
		ex, ey = self.m_Map.GetEnd()
		f = self.calF((x, y), (ex, ey))
		oInNode = CNode(x, y, 0, f)


		self.m_OpenQueue.push(oInNode)

		while not self.m_OpenQueue.empty():
			oNode = self.m_OpenQueue.poll()

			x, y = oNode.getXY()

			if x == ex and y == ey:
				self.output(oNode)
				break

			for dx, dy in d_defines.EIGHT_DIRS:
				tx = x + dx
				ty = y + dy

				#不可到达
				if not self.m_Map.IsCantainer(tx, ty) or self.m_Map.IsChar(tx, ty, d_defines.TYPE_WALL):
					continue

				cost = oNode.getCost() + self.calCost((x, y), (tx, ty))
				f = self.calF((tx, ty), (ex, ey))
				oNewNode = CNode(tx, ty, cost, f)
				oNewNode.setPreviousNode(oNode)

				#在关闭列表中，直接不处理
				if self.m_CloseQueue.container(oNewNode):
					continue

				oContainerNode = self.m_OpenQueue.containerNode(oNewNode)
				#节点在开开放列表时
				if oContainerNode:
					if oNewNode.G() < oContainerNode.G():
						oContainerNode.setCost(cost)
						oContainerNode.setFValue(f)
						oContainerNode.setPreviousNode(oNode)
						self.m_OpenQueue.update(oContainerNode)
					continue

				self.m_OpenQueue.push(oNewNode)

			if (x, y) not in lPrint:
				lPrint.append((x, y))
			self.m_Map.Print(lPrint)
			time.sleep(0.3)
			self.m_CloseQueue.push(oNode)

	def calCost(self, current, next):
		cx, cy = current
		nx, ny = next
		cost = math.sqrt((cx - nx) * (cx - nx) + (cy - ny) * (cy - ny)) * 10
		return cost

	def calF(self, current, end):
		cx, cy = current
		ex, ey = end

		return (abs(cx - ex) + abs(cy - ey)) * 10

	def output(self, oNode):
		lst = []
		while oNode:
			lst.append(oNode.getXY())
			oNode = oNode.getPreviousNode()

		lst = lst[-1::-1]
		self.m_Map.PrintWithPath(lst)

	def isInVisited(self, x, y):
		return (x, y) in self.m_CloseList






