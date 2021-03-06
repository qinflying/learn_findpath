#-*- coding:utf-8 -*-
import defines
import basemap
import time

class CMap(basemap.CMap):
	ROW = 9
	COL = 9
	def __init__(self):
		basemap.CMap.__init__(self)
		self.m_Books = {}
		self.m_MiniStep = 99999
		self.m_lPath = []
		self.InitMaps()

	def SetBook(self, x, y, book):
		self.m_Books[(x, y)] = book 

	def GetBook(self, x, y):
		return self.m_Books.get((x, y), 0)

	def SetMiniStep(self, step):
		self.m_MiniStep = step

	def GetMiniStep(self):
		return self.m_MiniStep

	def SetPaths(self, paths):
		self.m_lPath = paths[:]

	def ClearDFS(self):
		self.m_MiniStep = 99999
		self.m_dPath = []
		self.m_Books = {}

	def InitMaps(self):
		for i in xrange(self.ROW):
			for j in xrange(self.COL):
				if i == 0 or i == self.ROW -1 or j == 0 or j == self.COL-1:
					self.m_Maps[(i, j)] = defines.WALL_C
				else:
					self.m_Maps[(i, j)] = defines.EMPTY

		self.m_Hero = (2, 2)
		self.m_Maps[(2, 2)] = defines.HERO_C
		self.m_End = (7, 7)
		self.m_Maps[(7, 7)] = defines.END_C

		self.m_Maps[(2, 4)] = defines.WALL_C
		self.m_Maps[(3, 4)] = defines.WALL_C
		self.m_Maps[(4, 4)] = defines.WALL_C
		self.m_Maps[(5, 4)] = defines.WALL_C
		self.m_Maps[(7, 2)] = defines.WALL_C
		self.m_Maps[(6, 3)] = defines.WALL_C

	def Print(self):
		self.ClearPrint()
		for i in xrange(self.ROW):
			for j in xrange(self.COL):
				book = self.GetBook(i, j)
				if book:
					e = defines.PATH_C
				else:
					e = self.m_Maps[(i, j)]
				self.PrintOne(e)
			self.PrintOne("\n")

	def PrintWithPath(self):
		self.ClearPrint()
		iLength = len(self.m_lPath)
		for idx in xrange(iLength):
			time.sleep(0.1)
			self.ClearPrint()
			paths = self.m_lPath[:idx]
			for i in xrange(self.ROW):
				for j in xrange(self.COL):
					if (i, j) in paths:
						e = defines.PATH_C
					else:
						e = self.m_Maps[(i, j)]
					self.PrintOne(e)
				self.PrintOne("\n")







