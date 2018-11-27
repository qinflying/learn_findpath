#-*- coding:utf-8 -*-
import defines
import basemap

class CMap(basemap.CMap):
	ROW = 9
	COL = 9
	def __init__(self):
		basemap.CMap.__init__(self)
		self.m_Books = {}
		self.InitMaps()

	def SetBook(self, x, y, book):
		self.m_Books[(x, y)] = book 

	def GetBook(self, x, y):
		return self.m_Books.get((x, y), 0)

	def ClearBooks(self):
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
		self.m_Maps[(7, 7)] = defines.END_C

		self.m_Maps[(2, 4)] = defines.WALL_C
		self.m_Maps[(3, 4)] = defines.WALL_C
		self.m_Maps[(4, 4)] = defines.WALL_C
		self.m_Maps[(5, 4)] = defines.WALL_C

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






