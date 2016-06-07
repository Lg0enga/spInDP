from leg import Leg
import math
import dynamixel
import random
import time

class IK(object):

    def __init__(self):

        serial = dynamixel.SerialStream(port="/dev/USB2AX",
                                        baudrate="1000000",
                                        timeout=1)

        self.net = dynamixel.DynamixelNetwork(serial)

        servos = [32, 40, 41, 10, 11, 12, 61, 50, 51, 20, 21, 22, 62, 52, 60, 42, 30, 31]

        for servoId in servos:
            newDynamixel = dynamixel.Dynamixel(servoId, self.net)
            self.net._dynamixel_map[servoId] = newDynamixel

        self._rideHeight = 100
        self._initLegStretch = 150  #CoxaFootDist
        self._servoUpdatePeriod = 13

        self._X_COXA        =   122 #MM between front and back legs /2
        self._Y_COXA_FB     =   61  #MM between front/back legs /2
        self._Y_COXA_M      =   104 #MM between two middle legs /2
        self._COXA_ANGLE    =   45  #Angle of coxa from straight

        self._LENGTH_COXA   =   53  #MM distance from coxa servo to femur servo
        self._LENGTH_FEMUR  =   83  #MM distance from femur servo to tibia servo
        self._LENGTH_TIBIA  =   151.5 #MM distance from tibia servo to foot

        self.legs = []
        self.caseStep = []
        self._tick = 0

    #Initialize default foot positions
    def initInitialPositions(self):
        leg_right_front = Leg(0)
        leg_right_front.setInitialFootPosX(round(math.sin(math.radians(self._COXA_ANGLE))*self._initLegStretch))
        leg_right_front.setInitialFootPosY(round(math.cos(math.radians(self._COXA_ANGLE))*self._initLegStretch))
        leg_right_front.setInitialFootPosZ(self._rideHeight)
        leg_right_front.setLegBasePosX(self._X_COXA)
        leg_right_front.setLegBasePosY(self._Y_COXA_FB)
        leg_right_front.setLegBasePosZ(0)
        self.legs.append(leg_right_front)

        leg_right_middle = Leg(1)
        leg_right_middle.setInitialFootPosX(0)
        leg_right_middle.setInitialFootPosY(self._initLegStretch)
        leg_right_middle.setInitialFootPosZ(self._rideHeight)
        leg_right_middle.setLegBasePosX(0)
        leg_right_middle.setLegBasePosY(self._Y_COXA_M)
        leg_right_middle.setLegBasePosZ(0)
        self.legs.append(leg_right_middle)

        leg_right_rear = Leg(2)
        leg_right_rear.setInitialFootPosX(-round(math.sin(math.radians(self._COXA_ANGLE))*self._initLegStretch))
        leg_right_rear.setInitialFootPosY(round(math.cos(math.radians(self._COXA_ANGLE))*self._initLegStretch))
        leg_right_rear.setInitialFootPosZ(self._rideHeight)
        leg_right_rear.setLegBasePosX(-self._X_COXA) #min vergeten
        leg_right_rear.setLegBasePosY(self._Y_COXA_FB)
        leg_right_rear.setLegBasePosZ(0)
        self.legs.append(leg_right_rear)

        leg_left_rear = Leg(3)
        leg_left_rear.setInitialFootPosX(-round(math.sin(math.radians(self._COXA_ANGLE))*self._initLegStretch))
        leg_left_rear.setInitialFootPosY(-round(math.cos(math.radians(self._COXA_ANGLE))*self._initLegStretch))
        leg_left_rear.setInitialFootPosZ(self._rideHeight)
        leg_left_rear.setLegBasePosX(-self._X_COXA)
        leg_left_rear.setLegBasePosY(-self._Y_COXA_FB)
        leg_left_rear.setLegBasePosZ(0)
        self.legs.append(leg_left_rear)

        leg_left_middle = Leg(4)
        leg_left_middle.setInitialFootPosX(0)
        leg_left_middle.setInitialFootPosY(-self._initLegStretch)
        leg_left_middle.setInitialFootPosZ(self._rideHeight)
        leg_left_middle.setLegBasePosX(0)
        leg_left_middle.setLegBasePosY(-self._Y_COXA_M)
        leg_left_middle.setLegBasePosZ(0)
        self.legs.append(leg_left_middle)

        leg_left_front = Leg(5)
        leg_left_front.setInitialFootPosX(round(math.sin(math.radians(self._COXA_ANGLE))*self._initLegStretch))
        leg_left_front.setInitialFootPosY(-round(math.cos(math.radians(self._COXA_ANGLE))*self._initLegStretch))
        leg_left_front.setInitialFootPosZ(self._rideHeight)
        leg_left_front.setLegBasePosX(self._X_COXA)
        leg_left_front.setLegBasePosY(-self._Y_COXA_FB)
        leg_left_front.setLegBasePosZ(0)
        self.legs.append(leg_left_front)

    #Initialize crab foot positions
    def initInitialPositionsCrab(self):
        leg_right_front = Leg(0)
        leg_right_front.setInitialFootPosX(0)
        leg_right_front.setInitialFootPosY(self._initLegStretch)
        leg_right_front.setInitialFootPosZ(self._rideHeight)
        leg_right_front.setLegBasePosX(self._X_COXA)
        leg_right_front.setLegBasePosY(self._Y_COXA_FB)
        leg_right_front.setLegBasePosZ(0)
        self.legs.append(leg_right_front)

        leg_right_middle = Leg(1)
        leg_right_middle.setInitialFootPosX(0)
        leg_right_middle.setInitialFootPosY(self._initLegStretch)
        leg_right_middle.setInitialFootPosZ(self._rideHeight)
        leg_right_middle.setLegBasePosX(0)
        leg_right_middle.setLegBasePosY(self._Y_COXA_M)
        leg_right_middle.setLegBasePosZ(0)
        self.legs.append(leg_right_middle)

        leg_right_rear = Leg(2)
        leg_right_rear.setInitialFootPosX(0)
        leg_right_rear.setInitialFootPosY(self._initLegStretch)
        leg_right_rear.setInitialFootPosZ(self._rideHeight)
        leg_right_rear.setLegBasePosX(-self._X_COXA)
        leg_right_rear.setLegBasePosY(self._Y_COXA_FB)
        leg_right_rear.setLegBasePosZ(0)
        self.legs.append(leg_right_rear)

        leg_left_rear = Leg(3)
        leg_left_rear.setInitialFootPosX(0)
        leg_left_rear.setInitialFootPosY(-self._initLegStretch)
        leg_left_rear.setInitialFootPosZ(self._rideHeight)
        leg_left_rear.setLegBasePosX(-self._X_COXA)
        leg_left_rear.setLegBasePosY(-self._Y_COXA_FB)
        leg_left_rear.setLegBasePosZ(0)
        self.legs.append(leg_left_rear)

        leg_left_middle = Leg(4)
        leg_left_middle.setInitialFootPosX(0)
        leg_left_middle.setInitialFootPosY(-self._initLegStretch)
        leg_left_middle.setInitialFootPosZ(self._rideHeight)
        leg_left_middle.setLegBasePosX(0)
        leg_left_middle.setLegBasePosY(-self._Y_COXA_M)
        leg_left_middle.setLegBasePosZ(0)
        self.legs.append(leg_left_middle)

        leg_left_front = Leg(5)
        leg_left_front.setInitialFootPosX(0)
        leg_left_front.setInitialFootPosY(-self._initLegStretch)
        leg_left_front.setInitialFootPosZ(self._rideHeight)
        leg_left_front.setLegBasePosX(self._X_COXA)
        leg_left_front.setLegBasePosY(-self._Y_COXA_FB)
        leg_left_front.setLegBasePosZ(0)
        self.legs.append(leg_left_front)

    #Clear the casesteps when going to another walk movement
    def clearCaseSteps(self):
        self.caseStep = []

    #Tripod move
    def initTripod(self, xSpeed, ySpeed, rSpeed):
        self.caseStep.append(1)
        self.caseStep.append(2)
        self.caseStep.append(1)
        self.caseStep.append(2)
        self.caseStep.append(1)
        self.caseStep.append(2)
        rotSpeedOffsetX = []
        rotSpeedOffsetY = []

        if (abs(xSpeed) > 100) or (abs(ySpeed) > 100) or (abs(rSpeed) > 100):
            duration = 250 #duration of pull back step cycle (ms)
            numTicks = int(round(duration / self._servoUpdatePeriod)) #number of ticks in pull back step cycle

            speedX = 300 * xSpeed / 1023 #300mm/s step
            speedY = 300 * ySpeed / 1023 #300mm/s step
            speedR = 30 * rSpeed / 2000 #30 degrees/s top rotation speed

            amplitudeX = (speedX * duration / 1000.0) / 2.0
            amplitudeY = (speedY * duration / 1000.0) / 2.0

            if abs(rSpeed) > abs(xSpeed) and abs(rSpeed) > abs(ySpeed):
                amplitudeZ = -abs(50 * rSpeed / 1023)
            elif abs(xSpeed) > abs(ySpeed):
                amplitudeZ = -abs(50 * xSpeed / 1023)
            else:
                amplitudeZ = -abs(50 * ySpeed / 1023)

            for leg in self.legs:
                gblInitFootPosX = leg.getInitialFootPosX() + leg.getLegBasePosX()
                gblInitFootPosY = leg.getInitialFootPosY() + leg.getLegBasePosY()

                caseStep = self.caseStep[leg.getID()]

                if caseStep == 1:
                    #case 1 step forward

                    sinRotZ = math.sin(-math.radians(-speedR / 2.0 + speedR * (float(self._tick / numTicks))))
                    cosRotZ = math.cos(-math.radians(-speedR / 2.0 + speedR * (float(self._tick / numTicks))))

                    rotSpeedOffsetX.append(gblInitFootPosX * cosRotZ - gblInitFootPosY * sinRotZ - gblInitFootPosX)
                    rotSpeedOffsetY.append(gblInitFootPosX * sinRotZ + gblInitFootPosY * cosRotZ - gblInitFootPosY)

                    leg.setFootPosX(-amplitudeX * math.cos(math.pi * self._tick / numTicks) + rotSpeedOffsetX[leg.getID()])
                    leg.setFootPosY(-amplitudeY * math.cos(math.pi * self._tick / numTicks) + rotSpeedOffsetY[leg.getID()])
                    leg.setFootPosZ(amplitudeZ * math.sin(math.pi * self._tick / numTicks))

                    if self._tick >= numTicks - 1:
                        self.caseStep[leg.getID()] = 2

                if caseStep == 2:
                    #case 2 step backward

                    sinRotZ = math.sin(-math.radians(speedR / 2.0 - speedR * (float(self._tick / numTicks))))
                    cosRotZ = math.cos(-math.radians(speedR / 2.0 - speedR * (float(self._tick / numTicks))))

                    rotSpeedOffsetX.append(gblInitFootPosX * cosRotZ - gblInitFootPosY * sinRotZ - gblInitFootPosX)
                    rotSpeedOffsetY.append(gblInitFootPosX * sinRotZ + gblInitFootPosY * cosRotZ - gblInitFootPosY)

                    leg.setFootPosX(amplitudeX - 2 * amplitudeX * self._tick / numTicks + rotSpeedOffsetX[leg.getID()])
                    leg.setFootPosY(amplitudeY - 2 * amplitudeY * self._tick / numTicks + rotSpeedOffsetY[leg.getID()])
                    leg.setFootPosZ(0)

                    if self._tick >= numTicks - 1:
                        self.caseStep[leg.getID()] = 1

            if self._tick < numTicks -1:
                self._tick += 1
            else:
                self._tick = 0


    def initRipple(self, xSpeed, ySpeed, rSpeed):
        self.caseStep.append(2)
        self.caseStep.append(6)
        self.caseStep.append(4)
        self.caseStep.append(1)
        self.caseStep.append(3)
        self.caseStep.append(5)
        rotSpeedOffsetX = []
        rotSpeedOffsetY = []

        if (abs(xSpeed) > 5 * 8) or (abs(ySpeed) > 5 * 8) or (abs(rSpeed) > 5 * 8):
            duration = 125
            numTicks = int(round(duration / self._servoUpdatePeriod))
            numCasesPb = 4
            #print self._tick, numTicks

            speedX = 200 * xSpeed / 1023
            speedY = 200 * ySpeed / 1023
            speedR = 30 * rSpeed / 1023

            amplitudeX = (speedX * duration * numCasesPb / 1000.0) / 2.0
            amplitudeY = (speedY * duration * numCasesPb / 1000.0) / 2.0

            if abs(rSpeed) > abs(xSpeed) and abs(rSpeed) > abs(ySpeed):
                amplitudeZ = -abs(50 * rSpeed / 1023)
            elif abs(xSpeed) > abs(ySpeed):
                amplitudeZ = -abs(50 * xSpeed / 1023)
            else:
                amplitudeZ = -abs(50 * ySpeed / 1023)
            for leg in self.legs:
                gblInitFootPosX = leg.getInitialFootPosX() + leg.getLegBasePosX()
                gblInitFootPosY = leg.getInitialFootPosY() + leg.getLegBasePosY()

                caseStep = self.caseStep[leg.getID()]

                if caseStep == 1:
                    sinRotZ = math.sin(-math.radians(-speedR / 2.0 + speedR * (float(self._tick / numTicks))))
                    cosRotZ = math.cos(-math.radians(-speedR / 2.0 + speedR * (float(self._tick / numTicks))))

                    rotSpeedOffsetX.append(gblInitFootPosX * cosRotZ - gblInitFootPosY * sinRotZ - gblInitFootPosX)
                    rotSpeedOffsetY.append(gblInitFootPosX * sinRotZ + gblInitFootPosY * cosRotZ - gblInitFootPosY)

                    leg.setFootPosX(round(-amplitudeX * math.cos(math.pi * self._tick / (2.0 *numTicks)) + rotSpeedOffsetX[leg.getID()]))
                    leg.setFootPosY(round(-amplitudeY * math.cos(math.pi * self._tick / (2.0 *numTicks)) + rotSpeedOffsetY[leg.getID()]))
                    leg.setFootPosZ(round(amplitudeZ * math.sin(math.pi * self._tick / (2.0 *numTicks))))

                    #print leg.getID(), leg.getFootPosX(), leg.getFootPosY(), leg.getFootPosZ()

                    if self._tick >= numTicks - 1:
                        self.caseStep[leg.getID()] = 2

                if caseStep == 2:
                    sinRotZ = math.sin(-math.radians(speedR / 2.0 + speedR * (float(self._tick + numTicks)) / (float(2.0 * numTicks))))
                    cosRotZ = math.cos(-math.radians(speedR / 2.0 + speedR * (float(self._tick + numTicks)) / (float(2.0 * numTicks))))

                    rotSpeedOffsetX.append(gblInitFootPosX * cosRotZ - gblInitFootPosY * sinRotZ - gblInitFootPosX)
                    rotSpeedOffsetY.append(gblInitFootPosX * sinRotZ + gblInitFootPosY * cosRotZ - gblInitFootPosY)

                    leg.setFootPosX(round(-amplitudeX * math.cos(math.pi * (self._tick + numTicks) / (2.0 * numTicks))  + rotSpeedOffsetX[leg.getID()]))
                    leg.setFootPosY(round(-amplitudeY * math.cos(math.pi * (self._tick + numTicks) / (2.0 * numTicks))  + rotSpeedOffsetY[leg.getID()]))
                    leg.setFootPosZ(round(amplitudeZ * math.sin(math.pi * (self._tick + numTicks) / (2.0 * numTicks))))

                    if self._tick >= numTicks - 1:
                        self.caseStep[leg.getID()] = 3

                if caseStep == 3:
                    sinRotZ = math.sin(-math.radians(speedR / 2.0 - speedR * (float(self._tick + numTicks)) / (float(4.0 * numTicks))))
                    cosRotZ = math.cos(-math.radians(speedR / 2.0 - speedR * (float(self._tick + numTicks)) / (float(4.0 * numTicks))))

                    rotSpeedOffsetX.append(gblInitFootPosX * cosRotZ - gblInitFootPosY * sinRotZ - gblInitFootPosX)
                    rotSpeedOffsetY.append(gblInitFootPosX * sinRotZ + gblInitFootPosY * cosRotZ - gblInitFootPosY)

                    leg.setFootPosX(round(amplitudeX - 2.0 * amplitudeX * self._tick / (4.0 * numTicks) + rotSpeedOffsetX[leg.getID()]))
                    leg.setFootPosY(round(amplitudeY - 2.0 * amplitudeY * self._tick / (4.0 * numTicks) + rotSpeedOffsetY[leg.getID()]))
                    leg.setFootPosZ(0)

                    if self._tick >= numTicks - 1:
                        self.caseStep[leg.getID()] = 4

                if caseStep == 4:
                    sinRotZ = math.sin(-math.radians(speedR / 2.0 - speedR * (float(self._tick + numTicks)) / (float(4.0 * numTicks))))
                    cosRotZ = math.cos(-math.radians(speedR / 2.0 - speedR * (float(self._tick + numTicks)) / (float(4.0 * numTicks))))

                    rotSpeedOffsetX.append(gblInitFootPosX * cosRotZ - gblInitFootPosY * sinRotZ - gblInitFootPosX)
                    rotSpeedOffsetY.append(gblInitFootPosX * sinRotZ + gblInitFootPosY * cosRotZ - gblInitFootPosY)

                    leg.setFootPosX(round(amplitudeX - 2.0 * amplitudeX * (self._tick + numTicks) / (4.0 * numTicks) + rotSpeedOffsetX[leg.getID()]))
                    leg.setFootPosY(round(amplitudeY - 2.0 * amplitudeY * (self._tick + numTicks) / (4.0 * numTicks) + rotSpeedOffsetY[leg.getID()]))
                    leg.setFootPosZ(0)

                    if self._tick >= numTicks - 1:
                        self.caseStep[leg.getID()] = 5

                if caseStep == 5:
                    sinRotZ = math.sin(-math.radians(speedR / 2.0 - speedR * (float(self._tick + 2.0 * numTicks)) / (float(4.0 * numTicks))))
                    cosRotZ = math.cos(-math.radians(speedR / 2.0 - speedR * (float(self._tick + 2.0 * numTicks)) / (float(4.0 * numTicks))))

                    rotSpeedOffsetX.append(gblInitFootPosX * cosRotZ - gblInitFootPosY * sinRotZ - gblInitFootPosX)
                    rotSpeedOffsetY.append(gblInitFootPosX * sinRotZ + gblInitFootPosY * cosRotZ - gblInitFootPosY)

                    leg.setFootPosX(round(amplitudeX - 2.0 * amplitudeX * (self._tick + 2.0 * numTicks) / (4.0 * numTicks) + rotSpeedOffsetX[leg.getID()]))
                    leg.setFootPosY(round(amplitudeY - 2.0 * amplitudeY * (self._tick + 2.0 * numTicks) / (4.0 * numTicks) + rotSpeedOffsetY[leg.getID()]))
                    leg.setFootPosZ(0)

                    if self._tick >= numTicks - 1:
                        self.caseStep[leg.getID()] = 6

                if caseStep == 6:
                    sinRotZ = math.sin(-math.radians(speedR / 2.0 - speedR * (float(self._tick + 3.0 * numTicks)) / (float(4.0 * numTicks))))
                    cosRotZ = math.cos(-math.radians(speedR / 2.0 - speedR * (float(self._tick + 3.0 * numTicks)) / (float(4.0 * numTicks))))

                    rotSpeedOffsetX.append(gblInitFootPosX * cosRotZ - gblInitFootPosY * sinRotZ - gblInitFootPosX)
                    rotSpeedOffsetY.append(gblInitFootPosX * sinRotZ + gblInitFootPosY * cosRotZ - gblInitFootPosY)

                    leg.setFootPosX(round(amplitudeX - 2.0 * amplitudeX * (self._tick + 3.0 * numTicks) / (4.0 * numTicks) + rotSpeedOffsetX[leg.getID()]))
                    leg.setFootPosY(round(amplitudeY - 2.0 * amplitudeY * (self._tick + 3.0 * numTicks) / (4.0 * numTicks) + rotSpeedOffsetY[leg.getID()]))
                    leg.setFootPosZ(0)

                    if self._tick >= numTicks - 1:
                        self.caseStep[leg.getID()] = 1
            if self._tick < numTicks -1:
                self._tick += 1
            else:
                self._tick = 0

    def initWave(self, xSpeed, ySpeed, rSpeed):
        self.caseStep.append(4)
        self.caseStep.append(5)
        self.caseStep.append(6)
        self.caseStep.append(3)
        self.caseStep.append(2)
        self.caseStep.append(1)
        rotSpeedOffsetX = []
        rotSpeedOffsetY = []

        if (abs(xSpeed) > 5 * 8) or (abs(ySpeed) > 5 * 8) or (abs(rSpeed) > 5 * 8):
            duration = 500
            numTicks = int(round(duration / self._servoUpdatePeriod))
            numCasesPb = 5
            #print self._tick, numTicks

            speedX = 100 * xSpeed / 1023
            speedY = 100 * ySpeed / 1023
            speedR = 30 * rSpeed / 1023

            amplitudeX = (speedX * duration * numCasesPb / 1000.0) / 2.0
            amplitudeY = (speedY * duration * numCasesPb / 1000.0) / 2.0

            if abs(rSpeed) > abs(xSpeed) and abs(rSpeed) > abs(ySpeed):
                amplitudeZ = -abs(50 * rSpeed / 1023)
            elif abs(xSpeed) > abs(ySpeed):
                amplitudeZ = -abs(50 * xSpeed / 1023)
            else:
                amplitudeZ = -abs(50 * ySpeed / 1023)
            for leg in self.legs:
                gblInitFootPosX = leg.getInitialFootPosX() + leg.getLegBasePosX()
                gblInitFootPosY = leg.getInitialFootPosY() + leg.getLegBasePosY()

                caseStep = self.caseStep[leg.getID()]
                if caseStep == 1:

                    sinRotZ = math.sin(-math.radians(-speedR / 2.0 + speedR * float(self._tick) / float(numTicks)))
                    cosRotZ = math.cos(-math.radians(-speedR / 2.0 + speedR * float(self._tick) / float(numTicks)))

                    rotSpeedOffsetX.append(gblInitFootPosX * cosRotZ - gblInitFootPosY * sinRotZ - gblInitFootPosX)
                    rotSpeedOffsetY.append(gblInitFootPosX * sinRotZ + gblInitFootPosY * cosRotZ - gblInitFootPosY)

                    leg.setFootPosX(round(-amplitudeX * math.cos(math.pi * self._tick / numTicks) + rotSpeedOffsetX[leg.getID()]))
                    leg.setFootPosY(round(-amplitudeY * math.cos(math.pi * self._tick / numTicks) + rotSpeedOffsetY[leg.getID()]))
                    leg.setFootPosZ(round(amplitudeZ * math.sin(math.pi * self._tick / numTicks)))

                    #print leg.getID(), leg.getFootPosX(), leg.getFootPosY(), leg.getFootPosZ()

                    if self._tick >= numTicks - 1:
                        self.caseStep[leg.getID()] = 2

                if caseStep == 2:

                    sinRotZ = math.sin(-math.radians(speedR / 2.0 - speedR * float(self._tick) / float((5.0 * numTicks))))
                    cosRotZ = math.cos(-math.radians(speedR / 2.0 - speedR * float(self._tick) / float((5.0 * numTicks))))

                    rotSpeedOffsetX.append(gblInitFootPosX * cosRotZ - gblInitFootPosY * sinRotZ - gblInitFootPosX)
                    rotSpeedOffsetY.append(gblInitFootPosX * sinRotZ + gblInitFootPosY * cosRotZ - gblInitFootPosY)

                    leg.setFootPosX(round(amplitudeX - 2.0 * amplitudeX * self._tick / (5.0 * numTicks) + rotSpeedOffsetX[leg.getID()]))
                    leg.setFootPosX(round(amplitudeY - 2.0 * amplitudeY * self._tick / (5.0 * numTicks) + rotSpeedOffsetY[leg.getID()]))
                    leg.setFootPosZ(0)

                    if self._tick >= numTicks - 1:
                        self.caseStep[leg.getID()] = 3

                if caseStep == 3:

                    sinRotZ = math.sin(-math.radians(speedR / 2.0 - speedR * (float(self._tick + numTicks)) / (float(5.0 * numTicks))))
                    cosRotZ = math.cos(-math.radians(speedR / 2.0 - speedR * (float(self._tick + numTicks)) / (float(5.0 * numTicks))))

                    rotSpeedOffsetX.append(gblInitFootPosX * cosRotZ - gblInitFootPosY * sinRotZ - gblInitFootPosX)
                    rotSpeedOffsetY.append(gblInitFootPosX * sinRotZ + gblInitFootPosY * cosRotZ - gblInitFootPosY)

                    leg.setFootPosX(round(amplitudeX - 2.0 * amplitudeX * (self._tick + numTicks) / (5.0 * numTicks) + rotSpeedOffsetX[leg.getID()]))
                    leg.setFootPosY(round(amplitudeY - 2.0 * amplitudeY * (self._tick + numTicks) / (5.0 * numTicks) + rotSpeedOffsetY[leg.getID()]))
                    leg.setFootPosZ(0)

                    if self._tick >= numTicks - 1:
                        self.caseStep[leg.getID()] = 4

                if caseStep == 4:

                    sinRotZ = math.sin(-math.radians(speedR / 2.0 - speedR * (float(self._tick + 2.0 * numTicks)) / (float(5.0 * numTicks))))
                    cosRotZ = math.cos(-math.radians(speedR / 2.0 - speedR * (float(self._tick + 2.0 * numTicks)) / (float(5.0 * numTicks))))

                    rotSpeedOffsetX.append(gblInitFootPosX * cosRotZ - gblInitFootPosY * sinRotZ - gblInitFootPosX)
                    rotSpeedOffsetY.append(gblInitFootPosX * sinRotZ + gblInitFootPosY * cosRotZ - gblInitFootPosY)

                    leg.setFootPosX(round(amplitudeX - 2.0 * amplitudeX * (self._tick + 2.0 * numTicks) / (5.0 * numTicks) + rotSpeedOffsetX[leg.getID()]))
                    leg.setFootPosY(round(amplitudeY - 2.0 * amplitudeY * (self._tick + 2.0 * numTicks) / (5.0 * numTicks) + rotSpeedOffsetY[leg.getID()]))
                    leg.setFootPosZ(0)

                    if self._tick >= numTicks - 1:
                        self.caseStep[leg.getID()] = 5

                if caseStep == 5:

                    sinRotZ = math.sin(-math.radians(speedR / 2.0 - speedR * (float(self._tick + 3.0 * numTicks)) / (float(5.0 * numTicks))))
                    cosRotZ = math.cos(-math.radians(speedR / 2.0 - speedR * (float(self._tick + 3.0 * numTicks)) / (float(5.0 * numTicks))))

                    rotSpeedOffsetX.append(gblInitFootPosX * cosRotZ - gblInitFootPosY * sinRotZ - gblInitFootPosX)
                    rotSpeedOffsetY.append(gblInitFootPosX * sinRotZ + gblInitFootPosY * cosRotZ - gblInitFootPosY)

                    leg.setFootPosX(round(amplitudeX - 2.0 * amplitudeX * (self._tick + 3.0 * numTicks) / (5.0 * numTicks) + rotSpeedOffsetX[leg.getID()]))
                    leg.setFootPosY(round(amplitudeY - 2.0 * amplitudeY * (self._tick + 3.0 * numTicks) / (5.0 * numTicks) + rotSpeedOffsetY[leg.getID()]))
                    leg.setFootPosZ(0)

                    if self._tick >= numTicks - 1:
                        self.caseStep[leg.getID()] = 6

                if caseStep == 6:

                    sinRotZ = math.sin(-math.radians(speedR / 2.0 - speedR * (float(self._tick + 4.0 * numTicks)) / (float(4.0 * numTicks))))
                    cosRotZ = math.cos(-math.radians(speedR / 2.0 - speedR * (float(self._tick + 4.0 * numTicks)) / (float(4.0 * numTicks))))

                    rotSpeedOffsetX.append(gblInitFootPosX * cosRotZ - gblInitFootPosY * sinRotZ - gblInitFootPosX)
                    rotSpeedOffsetY.append(gblInitFootPosX * sinRotZ + gblInitFootPosY * cosRotZ - gblInitFootPosY)

                    leg.setFootPosX(round(amplitudeX - 2.0 * amplitudeX * (self._tick + 4.0 * numTicks) / (5.0 * numTicks) + rotSpeedOffsetX[leg.getID()]))
                    leg.setFootPosY(round(amplitudeY - 2.0 * amplitudeY * (self._tick + 4.0 * numTicks) / (5.0 * numTicks) + rotSpeedOffsetY[leg.getID()]))
                    leg.setFootPosZ(0)

                    if self._tick >= numTicks - 1:
                        self.caseStep[leg.getID()] = 1
            if self._tick < numTicks -1:
                self._tick += 1
            else:
                self._tick = 0

    #calculate necessary foot position to achieve body rotations, translations etc. mostly 0 (straight body)
    def bodyFK(self, rotX, rotY, rotZ, translationX, translationY, translationZ):
        bodyRotOffsetX = []
        bodyRotOffsetY = []
        bodyRotOffsetZ = []

        globalInitFootPosX = None
        globalInitFootPosY = None
        globalInitFootPosZ = None

        sinRotX = math.sin(math.radians(rotX))
        cosRotX = math.cos(math.radians(rotX))
        sinRotY = math.sin(math.radians(rotY))
        cosRotY = math.cos(math.radians(rotY))
        sinRotZ = math.sin(math.radians(rotZ))
        cosRotZ = math.cos(math.radians(rotZ))

        for leg in self.legs:

            #Distance from center of body to foot position
            globalInitFootPosX = leg.getInitialFootPosX() + leg.getLegBasePosX()
            globalInitFootPosY = leg.getInitialFootPosY() + leg.getLegBasePosY()
            globalInitFootPosZ = leg.getInitialFootPosZ() + leg.getLegBasePosZ()

            #Foot position offsets necessary to acheive given body rotation
            offsetX = (globalInitFootPosY * cosRotY * sinRotZ + globalInitFootPosY * cosRotZ * sinRotX * sinRotY + globalInitFootPosX * cosRotZ * cosRotY - globalInitFootPosX * sinRotZ * sinRotX * sinRotY - globalInitFootPosZ * cosRotX * sinRotY) - globalInitFootPosX
            offsetY = globalInitFootPosY * cosRotX * cosRotZ - globalInitFootPosX * cosRotX * sinRotZ + globalInitFootPosZ * sinRotX - globalInitFootPosY
            offsetZ = (globalInitFootPosY * sinRotZ * sinRotY - globalInitFootPosY * cosRotZ * cosRotY * sinRotX + globalInitFootPosX * cosRotZ * sinRotY + globalInitFootPosX * cosRotY * sinRotZ * sinRotX + globalInitFootPosZ * cosRotX * cosRotY) - globalInitFootPosZ

            #Calculated foot positions to acheive xlation/rotation input
            bodyRotOffsetX.append(leg.getInitialFootPosX() + offsetX - translationX + leg.getFootPosX())
            bodyRotOffsetY.append(leg.getInitialFootPosY() + offsetY - translationY + leg.getFootPosY())
            bodyRotOffsetZ.append(leg.getInitialFootPosZ() + offsetZ - translationZ + leg.getFootPosZ())

        #Rotates X and Y round the coxa to compensate for coxa mounting angles
        self.legs[0].setFootPosCalcX(bodyRotOffsetY[0] * math.cos(math.radians(self._COXA_ANGLE)) - bodyRotOffsetX[0] * math.sin(math.radians(self._COXA_ANGLE)))
        self.legs[0].setFootPosCalcY(bodyRotOffsetY[0] * math.sin(math.radians(self._COXA_ANGLE)) + bodyRotOffsetX[0] * math.cos(math.radians(self._COXA_ANGLE)))
        self.legs[0].setFootPosCalcZ(bodyRotOffsetZ[0])

        self.legs[1].setFootPosCalcX(bodyRotOffsetY[1] * math.cos(math.radians(self._COXA_ANGLE * 2)) - bodyRotOffsetX[1] * math.sin(math.radians(self._COXA_ANGLE * 2)))
        self.legs[1].setFootPosCalcY(bodyRotOffsetY[1] * math.sin(math.radians(self._COXA_ANGLE * 2)) + bodyRotOffsetX[1] * math.cos(math.radians(self._COXA_ANGLE * 2)))
        self.legs[1].setFootPosCalcZ(bodyRotOffsetZ[1])

        self.legs[2].setFootPosCalcX(bodyRotOffsetY[2] * math.cos(math.radians(self._COXA_ANGLE * 3)) - bodyRotOffsetX[2] * math.sin(math.radians(self._COXA_ANGLE * 3)))
        self.legs[2].setFootPosCalcY(bodyRotOffsetY[2] * math.sin(math.radians(self._COXA_ANGLE * 3)) + bodyRotOffsetX[2] * math.cos(math.radians(self._COXA_ANGLE * 3)))
        self.legs[2].setFootPosCalcZ(bodyRotOffsetZ[2])

        self.legs[3].setFootPosCalcX(bodyRotOffsetY[3] * math.cos(math.radians(self._COXA_ANGLE * 5)) - bodyRotOffsetX[3] * math.sin(math.radians(self._COXA_ANGLE * 5)))
        self.legs[3].setFootPosCalcY(bodyRotOffsetY[3] * math.sin(math.radians(self._COXA_ANGLE * 5)) + bodyRotOffsetX[3] * math.cos(math.radians(self._COXA_ANGLE * 5)))
        self.legs[3].setFootPosCalcZ(bodyRotOffsetZ[3])

        self.legs[4].setFootPosCalcX(bodyRotOffsetY[4] * math.cos(math.radians(self._COXA_ANGLE * 6)) - bodyRotOffsetX[4] * math.sin(math.radians(self._COXA_ANGLE * 6)))
        self.legs[4].setFootPosCalcY(bodyRotOffsetY[4] * math.sin(math.radians(self._COXA_ANGLE * 6)) + bodyRotOffsetX[4] * math.cos(math.radians(self._COXA_ANGLE * 6)))
        self.legs[4].setFootPosCalcZ(bodyRotOffsetZ[4])

        self.legs[5].setFootPosCalcX(bodyRotOffsetY[5] * math.cos(math.radians(self._COXA_ANGLE * 7)) - bodyRotOffsetX[5] * math.sin(math.radians(self._COXA_ANGLE * 7)))
        self.legs[5].setFootPosCalcY(bodyRotOffsetY[5] * math.sin(math.radians(self._COXA_ANGLE * 7)) + bodyRotOffsetX[5] * math.cos(math.radians(self._COXA_ANGLE * 7)))
        self.legs[5].setFootPosCalcZ(bodyRotOffsetZ[5])

        self.legIK()

    def legIK(self):
        for leg in self.legs:

            coxaFootDist = math.sqrt(math.pow(leg.getFootPosCalcY(), 2) + math.pow(leg.getFootPosCalcX(), 2))

            ikSW = math.sqrt(math.pow(coxaFootDist - self._LENGTH_COXA, 2) + math.pow(leg.getFootPosCalcZ(), 2))

            ikA1 = math.atan2(leg.getFootPosCalcZ(), (coxaFootDist - self._LENGTH_COXA))

            if ikSW > self._LENGTH_TIBIA + self._LENGTH_FEMUR - 1:
                ikSW = self._LENGTH_TIBIA + self._LENGTH_FEMUR - 1

            ikA2 = math.acos( ( math.pow(self._LENGTH_FEMUR, 2) + math.pow(ikSW, 2) - math.pow(self._LENGTH_TIBIA, 2) ) / ( 2 * self._LENGTH_FEMUR * ikSW) )

            coxaAngle = math.atan2(leg.getFootPosCalcX(), leg.getFootPosCalcY())

            femurAngle = (ikA2 - ikA1)

            tibiaAngle = math.acos((math.pow(self._LENGTH_FEMUR, 2) + math.pow(self._LENGTH_TIBIA, 2) - math.pow(ikSW, 2) )/ ( 2 * self._LENGTH_FEMUR * self._LENGTH_TIBIA) )

            leg.setJointAngleCoxa(math.degrees(coxaAngle))
            leg.setJointAngleFemur(math.degrees(femurAngle))
            leg.setJointAngleTibia(90 - math.degrees(tibiaAngle))

        #corrections per side
        for i in range(0, 3):
            self.legs[i].setJointAngleCoxa((self.legs[i].getJointAngleCoxa() - 150))
            self.legs[i].setJointAngleFemur((self.legs[i].getJointAngleFemur() + 150))
            self.legs[i].setJointAngleTibia((self.legs[i].getJointAngleTibia() + 150))

        for i in range(3, 6):
            self.legs[i].setJointAngleCoxa((self.legs[i].getJointAngleCoxa() - 150))
            self.legs[i].setJointAngleFemur((self.legs[i].getJointAngleFemur() - 150))
            self.legs[i].setJointAngleTibia((self.legs[i].getJointAngleTibia() - 150))

        self.driveServos()

    #Calculate bits for servo positions
    def driveServos(self):
        for leg in self.legs:
            leg.setServoPosCoxa(round(abs(leg.getJointAngleCoxa()  * 3.41)))
            leg.setServoPosFemur(round(abs(leg.getJointAngleFemur() * 3.41)))
            leg.setServoPosTibia(round(abs(leg.getJointAngleTibia() * 3.41)))

        self.syncWriteServos()

    #write bits to servo's
    def syncWriteServos(self):
        speed = 1023

        actuator = self.net._dynamixel_map[40]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[0].getServoPosCoxa())
        actuator = self.net._dynamixel_map[41]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[0].getServoPosFemur())
        actuator = self.net._dynamixel_map[42]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[0].getServoPosTibia())

        actuator = self.net._dynamixel_map[50]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[1].getServoPosCoxa())
        actuator = self.net._dynamixel_map[51]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[1].getServoPosFemur())
        actuator = self.net._dynamixel_map[52]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[1].getServoPosTibia())

        actuator = self.net._dynamixel_map[60]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[2].getServoPosCoxa())
        actuator = self.net._dynamixel_map[61]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[2].getServoPosFemur())
        actuator = self.net._dynamixel_map[62]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[2].getServoPosTibia())

        actuator = self.net._dynamixel_map[30]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[3].getServoPosCoxa())
        actuator = self.net._dynamixel_map[31]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[3].getServoPosFemur())
        actuator = self.net._dynamixel_map[32]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[3].getServoPosTibia())

        actuator = self.net._dynamixel_map[20]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[4].getServoPosCoxa())
        actuator = self.net._dynamixel_map[21]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[4].getServoPosFemur())
        actuator = self.net._dynamixel_map[22]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[4].getServoPosTibia())

        actuator = self.net._dynamixel_map[10]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[5].getServoPosCoxa())
        actuator = self.net._dynamixel_map[11]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[5].getServoPosFemur())
        actuator = self.net._dynamixel_map[12]
        actuator.moving_speed = speed
        actuator.goal_position = int(self.legs[5].getServoPosTibia())

        self.net.synchronize()
