#-*- coding:utf-8 -*-

class CState(object):
	def __init__(self):
		self.m_vPos = None 
		self.m_previousState = None 
		self.m_FValue = 0 
		self.m_Cost = 0

	def getPos(self):
		return self.m_vPos

	def setPos(self, vPos):
		self.m_vPos = vPos

	def getPreviousState(self):
		return self.m_previousState

	def setPreviousState(self, oState):
		self.m_previousState = oState

	def getFValue(self):
		return self.m_FValue

	def setFValue(self, v):
		self.m_FValue = v 

	def getCost(self):
		return self.m_Cost

	def setCost(self, v):
		self.m_Cost = v 

	def same(self, oState):
		#位置不同
		if self.m_vPos != oState.m_vPos:
			return False
		return True