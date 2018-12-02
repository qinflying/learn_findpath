#-*- coding:utf-8 -*-

class CNode(object):
	def __init__(self, x, y):
		self.m_X = x
		self.m_Y = y

	def setX(self, x):
		self.m_X = x 

	def setY(self, y):
		self.m_Y = y 

	def x(self):
		return self.m_X 

	def y(self):
		return self.m_Y

	def xy(self):
		return self.m_X, self.m_Y

	def same(self, node):
		return self.m_X == node.x() and self.m_Y == node.y()

	def clone(self):
		return CNode(self.m_X, self.m_Y)

	@staticmethod
	def isSame(node1, node2):
		return node1.same(node2)

	def __repr__(self):
		return "(node:%d, %d, %s)" % (self.m_X, self.m_Y, id(self))
