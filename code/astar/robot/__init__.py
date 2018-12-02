#-*- coding:utf-8 -*-
#扫地机器人
#https://blog.csdn.net/kwame211/article/details/78139506
from . import ui
from . import state
from .. import node
from . import r_defines
import time

def Demo():
	oRobot = CRobot()
	oRobot.work()

class CRobot(object):
	def __init_(self):
		#存放State的优先队列
		self.m_priorityQueue = CPriorityQueue()
		self.m_Map = ui.CMap()
		#已存在的State
		self.m_CloseList = []

	def Reset(self):
		#存放State的优先队列
		self.m_priorityQueue = CPriorityQueue()
		self.m_Map = ui.CMap()
		#已存在的State
		self.m_CloseList = []


	def work(self):
		self.Reset()
		self.m_Map.Print()
		dirtylst = self.m_Map.GetDirtyList()

		oInitState = state.CState()
		oInitState.setRobotLocation(self.m_Map.GetRobot())
		oInitState.setDirtList(dirtylst)
		oInitState.setCost(0)
		oInitState.setFValue(0+len(dirtylst))

		self.m_priorityQueue.push(oInitState)

		print dirtylst

		while not self.m_priorityQueue.empty():
			oState = self.m_priorityQueue.poll()

			if self.isGoal(oState):
				self.output(oState)
				break

			oRobotLocation = oState.getRobotLocation()
			x, y = oRobotLocation.xy()
			for dx, dy in r_defines.FOUR_DIRS:
				tx = x + dx 
				ty = y + dy
				targetNode = node.CNode(tx, ty)
				dirtylst = oState.getDirtList()

				#不可达
				if not self.m_Map.IsNodeContainer(targetNode) or self.m_Map.IsNodeType(targetNode, r_defines.TYPE_WALL):
					continue

				#清理灰尘
				if self.m_Map.IsNodeType(targetNode, r_defines.TYPE_DIRTY) and not self.isCleared(targetNode, dirtylst):
					dirtylst = self.clearDirtyOne(targetNode, dirtylst)

				oNewState = state.CState()
				oNewState.setRobotLocation(targetNode)
				oNewState.setDirtList(dirtylst)
				oNewState.setCost(oState.getCost() + 1)
				oNewState.setFValue(oNewState.getFValue() + len(dirtylst))
				oNewState.setPreviousState(oState)
				if not self.isDuplicated(oNewState):
					self.m_priorityQueue.push(oNewState)
					self.m_CloseList.append(oNewState)

					paths = [o.getRobotLocation().xy() for o in self.m_CloseList]
					#self.m_Map.Print(paths)
					#time.sleep(0.1)

	def output(self, oState):
		lst = []
		while oState:
			lst.append(oState.getRobotLocation().xy())
			oState = oState.getPreviousState()

		lst = lst[-1::-1]
		self.m_Map.PrintWithPath(lst)

	def isGoal(self, oState):
		return oState.isDirtEmpty()

	def isDuplicated(self, oState):
		for ost in self.m_CloseList:
			if ost.same(oState):
				return True 
		return False

	def isCleared(self, oNode, dirtyLst):
		for d in dirtyLst:
			if d.same(oNode):
				return False 
		return True

	def clearDirtyOne(self, oNode, dirtylst):
		lst = []
		for d in dirtylst:
			if d.same(oNode):
				continue
			lst.append(d)
		return lst


class CPriorityQueue(object):
	def __init__(self):
		self.m_Queue = []

	def empty(self):
		return len(self.m_Queue) == 0

	def poll(self):
		oState = self.m_Queue.pop(0)
		return oState

	#F较小的State排在队列前面
	def push(self, oState):
		index = len(self.m_Queue)
		for i, o in enumerate(self.m_Queue):
			if o.getFValue() > oState.getFValue():
				index = i 
				break 
		self.m_Queue.insert(index, oState)
