#-*- coding:utf-8 -*-
from . import r_defines
from .. import node
import basemap
import time

class CMap(basemap.CMap):
	ROW = 9
	COL = 9
	def __init__(self):
		basemap.CMap.__init__(self)
		self.InitMaps()

	def InitMaps(self):
		for i in xrange(self.ROW):
			for j in xrange(self.COL):
				if i == 0 or i == self.ROW -1 or j == 0 or j == self.COL-1:
					self.m_Maps[(i, j)] = r_defines.TYPE_WALL
				else:
					self.m_Maps[(i, j)] = r_defines.TYPE_EMPTY

		self.m_Robot = (2, 2)
		self.m_Maps[(2, 2)] = r_defines.TYPE_ROBOT
		self.m_Maps[(7, 7)] = r_defines.TYPE_DIRTY
		self.m_Maps[(5, 5)] = r_defines.TYPE_DIRTY
		self.m_Maps[(7, 1)] = r_defines.TYPE_DIRTY

		self.m_Maps[(2, 4)] = r_defines.TYPE_WALL
		self.m_Maps[(3, 4)] = r_defines.TYPE_WALL
		#self.m_Maps[(4, 4)] = r_defines.TYPE_WALL
		self.m_Maps[(5, 4)] = r_defines.TYPE_WALL
		self.m_Maps[(7, 2)] = r_defines.TYPE_WALL
		self.m_Maps[(6, 3)] = r_defines.TYPE_WALL

	def IsNodeType(self, oNode, t):
		return self.m_Maps.get(oNode.xy()) == t

	def IsNodeContainer(self, oNode):
		return self.IsCantainer(*oNode.xy())

	def GetRobot(self):
		return node.CNode(*self.m_Robot)

	def GetDirtyList(self):
		lst = []
		for key, value in self.m_Maps.iteritems():
			if value == r_defines.TYPE_DIRTY:
				o = node.CNode(*key)
				lst.append(o)
		return lst

	def Print(self, paths = None):
		if paths is None:
			paths = []
		self.ClearPrint()
		for i in xrange(self.ROW):
			for j in xrange(self.COL):
				t = self.m_Maps[(i, j)]
				if t != r_defines.TYPE_ROBOT and (i, j) in paths:
					t = r_defines.TYPE_PATH
				self.PrintType(t)
			self.PrintContent("\n")

	def PrintWithPath(self, paths):
		print paths
		for idx in xrange(len(paths)):
			pa = paths[idx:idx+1]
			time.sleep(0.3)
			self.ClearPrint()
			for i in xrange(self.ROW):
				for j in xrange(self.COL):
					t = self.m_Maps[(i, j)]
					if t not in (r_defines.TYPE_ROBOT, r_defines.TYPE_DIRTY) and (i, j) in pa:
						t = r_defines.TYPE_PATH
					self.PrintType(t)
				self.PrintContent("\n")

	def PrintType(self, t):
		e = r_defines.I2CHAR.get(t, "")
		f = r_defines.I2FCOLOR.get(t, "")
		b = r_defines.I2BCOLOR.get(t, "")
		self.PrintContent(b+f+e)




