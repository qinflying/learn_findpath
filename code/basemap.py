#-*- coding:utf-8 -*-
import defines
import sys

class CMap(object):
	ROW = 9
	COL = 9
	def __init__(self):
		self.m_Hero = (0, 0)
		self.m_Maps = {}

	def IsCantainer(self, x, y):
		if x < 0 or x >= self.ROW:
			return False 
		if y < 0 or y >= self.COL:
			return False
		return True

	def IsChar(self, x, y, c):
		m = self.m_Maps.get((x, y))
		if m is None:
			return False 
		return c == m

	def Print(self):
		self.ClearPrint()
		for i in xrange(self.ROW):
			for j in xrange(self.COL):
				e = self.m_Maps[(i, j)]
				self.PrintOne(e)
			self.PrintOne("\n")

	def PrintOne(self, c):
		from colorama import Fore
		color = defines.C2COLOR.get(c, "")
		sys.stdout.write(color+c)
		

	def ClearPrint(self):
		import os
		os.system("cls")


