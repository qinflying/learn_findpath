#-*- coding:utf-8 -*-
from . import m_defines
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
					self.m_Maps[(i, j)] = m_defines.TYPE_WALL
				else:
					self.m_Maps[(i, j)] = m_defines.EMPTY

		self.m_Hero = (2, 2)
		self.m_Maps[(2, 2)] = m_defines.TYPE_HERO
		self.m_End = (7, 7)
		self.m_Maps[(7, 7)] = m_defines.TYPE_END

		self.m_Maps[(2, 4)] = m_defines.TYPE_WALL
		self.m_Maps[(3, 4)] = m_defines.TYPE_WALL
		self.m_Maps[(4, 4)] = m_defines.TYPE_WALL
		self.m_Maps[(5, 4)] = m_defines.TYPE_WALL
		self.m_Maps[(7, 2)] = m_defines.TYPE_WALL
		self.m_Maps[(6, 3)] = m_defines.TYPE_WALL

	def Print(self):
		self.ClearPrint()
		for i in xrange(self.ROW):
			for j in xrange(self.COL):
				e = self.m_Maps[(i, j)]
				self.PrintType(e)
			self.PrintOne("\n")

	def PrintType(self, t):
		e = r_defines.I2CHAR.get(t, "")
		f = r_defines.I2FCOLOR.get(t, "")
		b = r_defines.I2BCOLOR.get(t, "")
		self.PrintContent(b+f+e)