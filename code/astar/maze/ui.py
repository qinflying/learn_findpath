#-*- coding:utf-8 -*-
from . import d_defines
import basemap
import time

class CMap(basemap.CMap):
	ROW = 15
	COL = 15
	def __init__(self):
		basemap.CMap.__init__(self)
		self.InitMaps()

	def InitMaps(self):
		for i in xrange(self.ROW):
			for j in xrange(self.COL):
				if i == 0 or i == self.ROW -1 or j == 0 or j == self.COL-1:
					self.m_Maps[(i, j)] = d_defines.TYPE_WALL
				else:
					self.m_Maps[(i, j)] = d_defines.TYPE_EMPTY

		self.m_Hero = (8, 2)
		self.m_Maps[(8, 2)] = d_defines.TYPE_HERO
		self.m_End = (6, 12)
		self.m_Maps[(6, 12)] = d_defines.TYPE_END

		self.m_Maps[(5, 10)] = d_defines.TYPE_WALL
		self.m_Maps[(6, 10)] = d_defines.TYPE_WALL
		self.m_Maps[(7, 10)] = d_defines.TYPE_WALL
		self.m_Maps[(8, 10)] = d_defines.TYPE_WALL
		self.m_Maps[(5, 9)] = d_defines.TYPE_WALL
		self.m_Maps[(6, 9)] = d_defines.TYPE_WALL
		self.m_Maps[(7, 9)] = d_defines.TYPE_WALL
		self.m_Maps[(8, 9)] = d_defines.TYPE_WALL


	def GetHero(self):
		return self.m_Hero

	def GetEnd(self):
		return self.m_End

	def Print(self, paths = None):
		if paths is None:
			paths = []
		self.ClearPrint()
		for i in xrange(self.ROW):
			for j in xrange(self.COL):
				t = self.m_Maps[(i, j)]
				if t != d_defines.TYPE_HERO and (i, j) in paths:
					t = d_defines.TYPE_PATH
				self.PrintType(t)
			self.PrintContent("\n")

	def PrintWithPath(self, paths):
		print paths
		for idx in xrange(len(paths)):
			pa = paths[:idx+1]
			time.sleep(0.3)
			self.ClearPrint()
			for i in xrange(self.ROW):
				for j in xrange(self.COL):
					t = self.m_Maps[(i, j)]
					if t not in (d_defines.TYPE_HERO, d_defines.TYPE_END) and (i, j) in pa:
						t = d_defines.TYPE_PATH
					self.PrintType(t)
				self.PrintContent("\n")

	def PrintType(self, t):
		e = d_defines.I2CHAR.get(t, "")
		f = d_defines.I2FCOLOR.get(t, "")
		b = d_defines.I2BCOLOR.get(t, "")
		self.PrintContent(b+f+e)