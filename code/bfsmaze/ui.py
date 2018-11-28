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
		self.m_dPath = {}
		self.InitMaps()

	def SetBook(self, x, y, book):
		self.m_Books[(x, y)] = book 

	def GetBook(self, x, y):
		return self.m_Books.get((x, y), 0)

	def SetPaths(self, curx, cury, frontx, fronty):
		self.m_dPath[(curx, cury)] = (frontx, frontx)

	def ClearBFS(self):
		self.m_dPath = {}
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
		lPath = self.AnalysisPath()
		iLength = len(lPath)
		print lPath, self.m_dPath
		for idx in xrange(iLength):
			time.sleep(0.1)
			#self.ClearPrint()
			paths = lPath[:idx]
			for i in xrange(self.ROW):
				for j in xrange(self.COL):
					if (i, j) in paths:
						e = defines.PATH_C
					else:
						e = self.m_Maps[(i, j)]
					self.PrintOne(e)
				self.PrintOne("\n")

	def AnalysisPath(self):
		x, y = self.m_End
		lPath = []

		pos = self.m_dPath.get((x, y))

		while pos:

			#出现环状Bug
			if pos in lPath:
				break
			lPath.append(pos)

			pos = self.m_dPath.get(pos)
		return lPath[-1::-1]