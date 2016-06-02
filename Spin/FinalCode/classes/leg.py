class Leg(object):

    def __init__(self, iD):
        self.id = iD

    def getID(self):
        return self.id

    #Current foot positions

    def setFootPosX(self, footPosX):
        self.footPosX = footPosX

    def getFootPosX(self):
        if not hasattr(self, 'footPosX'):
            return 0
        else:
            return self.footPosX

    def setFootPosY(self, footPosY):
        self.footPosY = footPosY

    def getFootPosY(self):
        if not hasattr(self, 'footPosY'):
            return 0
        else:
            return self.footPosY

    def setFootPosZ(self, footPosZ):
        self.footPosZ = footPosZ

    def getFootPosZ(self):
        if not hasattr(self, 'footPosZ'):
            return 0
        else:
            return self.footPosZ

    #Initial foot positions

    def setInitialFootPosX(self, initialFootPosX):
        self.initialFootPosX = initialFootPosX

    def getInitialFootPosX(self):
        return self.initialFootPosX

    def setInitialFootPosY(self, initialFootPosY):
        self.initialFootPosY = initialFootPosY

    def getInitialFootPosY(self):
        return self.initialFootPosY

    def setInitialFootPosZ(self, initialFootPosZ):
        self.initialFootPosZ = initialFootPosZ

    def getInitialFootPosZ(self):
        return self.initialFootPosZ

    #Leg base positions

    def setLegBasePosX(self, legBasePosX):
        self.legBasePosX = legBasePosX

    def getLegBasePosX(self):
        return self.legBasePosX

    def setLegBasePosY(self, legBasePosY):
        self.legBasePosY = legBasePosY

    def getLegBasePosY(self):
        return self.legBasePosY

    def setLegBasePosZ(self, legBasePosZ):
        self.legBasePosZ = legBasePosZ

    def getLegBasePosZ(self):
        return self.legBasePosZ

    #Foot position calculations

    def setFootPosCalcX(self, footPosCalcX):
        self.footPosCalcX = footPosCalcX

    def getFootPosCalcX(self):
        return self.footPosCalcX

    def setFootPosCalcY(self, footPosCalcY):
        self.footPosCalcY = footPosCalcY

    def getFootPosCalcY(self):
        return self.footPosCalcY

    def setFootPosCalcZ(self, footPosCalcZ):
        self.footPosCalcZ = footPosCalcZ

    def getFootPosCalcZ(self):
        return self.footPosCalcZ

    #Joint angles

    def setJointAngleCoxa(self, jointAngleCoxa):
        self.jointAngleCoxa = jointAngleCoxa

    def getJointAngleCoxa(self):
        return self.jointAngleCoxa

    def setJointAngleFemur(self, jointAngleFemur):
        self.jointAngleFemur = jointAngleFemur

    def getJointAngleFemur(self):
        return self.jointAngleFemur

    def setJointAngleTibia(self, jointAngleTibia):
        self.jointAngleTibia = jointAngleTibia

    def getJointAngleTibia(self):
        return self.jointAngleTibia

    #Servo positions

    def setServoPosCoxa(self, servoPositionCoxa):
        self.servoPositionCoxa = servoPositionCoxa

    def getServoPosCoxa(self):
        return self.servoPositionCoxa

    def setServoPosFemur(self, servoPositionFemur):
        self.servoPositionFemur = servoPositionFemur

    def getServoPosFemur(self):
        return self.servoPositionFemur

    def setServoPosTibia(self, servoPositionTibia):
        self.servoPositionTibia = servoPositionTibia

    def getServoPosTibia(self):
        return self.servoPositionTibia

    #Body rotation Z

    def setBodyRotZ(self, bodyRotZ):
        self.bodyRotZ = bodyRotZ

    def getBodyRotZ(self):
        return bodyRotZ
