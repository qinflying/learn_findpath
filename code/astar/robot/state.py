#-*- coding:utf-8 -*-

class CState(object):
	def __init__(self):
		self.m_robotLocation = None 
		self.m_previousState = None 
		self.m_dirtList = []
		self.m_FValue = 0 
		self.m_Cost = 0

	def getRobotLocation(self):
		return self.m_robotLocation

	def setRobotLocation(self, oLocation):
		self.m_robotLocation = oLocation

	def getPreviousState(self):
		return self.m_previousState

	def setPreviousState(self, oState):
		self.m_previousState = oState

	def getDirtList(self):
		return self.m_dirtList[:]

	def setDirtList(self, dirtlist):
		self.m_dirtList = []
		for d in dirtlist:
			cd = d.clone()
			self.m_dirtList.append(cd)

	def isDirtEmpty(self):
		return len(self.m_dirtList) == 0

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
		if(not self.m_robotLocation.same(oState.getRobotLocation())):
			return False 
		#列表长度不同
		elif(len(self.m_dirtList) != len(oState.getDirtList())):
			return False
		else:
			dr1 = [o.xy() for o in self.m_dirtList]
			dr2 = [o.xy() for o in oState.getDirtList()]
			return set(dr1) == set(dr2)