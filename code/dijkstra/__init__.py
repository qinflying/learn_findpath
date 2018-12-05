#-*- coding:utf-8 -*-
#https://cloud.tencent.com/developer/news/261896
from . import ui 
import time
import math
MAX_COST = 999999
def Demo():
	oWork = CDijkstra()
	oWork.work()

class CNode(object):
	def __init__(self, x=0, y=0, cost=9999):
		self.m_X = x
		self.m_Y = y 
		self.m_Cost = cost 
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
			if e.getCost() > o.getCost():
				index = idx 
				break 

		self.m_Queue.insert(index, o)

	def update(self, o):
		if o in self.m_Queue:
			self.m_Queue.remove(o)
		self.push(o)

	def containerNode(self, o):
		for no in self.m_Queue:
			if no.getXY() == o.getXY():
				return no 
		return None

class CCloseQueue(object):
	def __init__(self):
		self.m_Queue = []
		self.m_XY = []

	def push(self, o):
		self.m_Queue.append(o)
		self.m_XY.append(o.getXY())

	def container(self, o):
		return o.getXY() in self.m_XY

class CDijkstra(object):
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
		oInitNode = CNode(x, y, 0)
		cost_so_far = {(x, y):0}

		self.m_OpenQueue.push(oInitNode)

		while not self.m_OpenQueue.empty():
			oNode = self.m_OpenQueue.poll()


			x, y = oNode.getXY()

			if x == ex and y == ey:
				self.output(oNode)
				break

			for dx, dy in d_defines.EIGHT_DIRS:
				tx = x + dx
				ty = y + dy

				#不可达
				if not self.m_Map.IsCantainer(tx, ty) or self.m_Map.IsChar(tx, ty, d_defines.TYPE_WALL):
					continue

				cost = cost_so_far.get((x, y), MAX_COST) + self.calCost((x, y), (tx, ty))
				oNewNode = CNode(tx, ty, cost)
				oNewNode.setPreviousNode(oNode)

				oContainerNode = self.m_OpenQueue.containerNode(oNewNode)
				#在关闭列表中，直接不处理
				if self.m_CloseQueue.container(oNewNode):
					continue
				#节点在开开放列表时
				if oContainerNode:
					if cost < oContainerNode.getCost():
						oContainerNode.setCost(cost)
						oContainerNode.setPreviousNode(oNode)
						self.m_OpenQueue.update(oContainerNode)
					continue

				self.m_OpenQueue.push(oNewNode)

				if (tx, ty) not in lPrint:
					lPrint.append((tx, ty))
				self.m_Map.Print(lPrint)
				time.sleep(0.05)

			self.m_CloseQueue.push(oNode)

	def calCost(self, current, next):
		cx, cy = current
		nx, ny = next

		#water会增加1个点的消耗
		if self.m_Map.IsChar(nx, ny, d_defines.TYPE_WATER):
			watercost = 10
		else:
			watercost = 0
		cost = watercost + math.sqrt((cx - nx) * (cx - nx) + (cy - ny) * (cy - ny)) * 10
		return cost

	def output(self, oNode):
		lst = []
		while oNode:
			lst.append(oNode.getXY())
			oNode = oNode.getPreviousNode()

		lst = lst[-1::-1]
		self.m_Map.PrintWithPath(lst)

	def isInVisited(self, x, y):
		return (x, y) in self.m_CloseList






