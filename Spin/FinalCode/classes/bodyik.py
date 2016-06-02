import dynamixel
import math
from leg import Leg

class BodyIK(object):

    def __init__(self):

        # serial = dynamixel.SerialStream(port="/dev/USB2AX",
        #                                 baudrate="1000000",
        #                                 timeout=1)
        #
        # self.net = dynamixel.DynamixelNetwork(serial)
        #
        # servos = [32, 40, 41, 10, 11, 12, 61, 50, 51, 20, 21, 22, 62, 52, 60, 42, 30, 31]
        #
        # for servoId in servos:
        #     newDynamixel = dynamixel.Dynamixel(servoId, self.net)
        #     self.net._dynamixel_map[servoId] = newDynamixel

        self.legs = []

        self._X_COXA = 122
        self._Y_COXA_FB = 61
        self._Y_COXA_M = 104
        self._COXA_ANGLE = 45

        self._LENGTH_COXA = 53
        self._LENGTH_FEMUR = 83
        self._LENGTH_TIBIA = 150

        self._initLegStretch = 20
        self._rideHeightOffset = -60

    def SetInitialValues(self):
        #RIGHT FRONT
        leg_right_front = Leg(0)
        leg_right_front.setInitialFootPositionX(round(math.sin(math.radians(self._COXA_ANGLE))*(self._LENGTH_COXA + self._LENGTH_FEMUR + self._initLegStretch)))
        leg_right_front.setInitialFootPositionY(round(math.cos(math.radians(self._COXA_ANGLE))*(self._LENGTH_COXA + self._LENGTH_FEMUR + self._initLegStretch)))
        leg_right_front.setInitialFootPositionZ(self._LENGTH_TIBIA + self._rideHeightOffset)
        leg_right_front.setLegBasePositionX = self._X_COXA
        leg_right_front.setLegBasePositionY = self._Y_COXA_FB
        leg_right_front.setLegBasePositionZ = 0
        self.legs.append(leg_right_front)

        #RIGHT MIDDLE
        leg_right_middle = Leg(1)
        leg_right_middle.setInitialFootPositionX(0)
        leg_right_middle.setInitialFootPositionY(self._LENGTH_COXA + self._LENGTH_FEMUR + self._initLegStretch)
        leg_right_middle.setInitialFootPositionZ(self._LENGTH_TIBIA + self._rideHeightOffset)
        leg_right_middle.setLegBasePositionX = 0
        leg_right_middle.setLegBasePositionY = self._Y_COXA_M
        leg_right_middle.setLegBasePositionZ = 0
        self.legs.append(leg_right_middle)

        #RIGHT REAR
        leg_right_rear = Leg(2)
        leg_right_rear.setInitialFootPositionX(round(math.sin(math.radians(-self._COXA_ANGLE))*(self._LENGTH_COXA + self._LENGTH_FEMUR + self._initLegStretch)))
        leg_right_rear.setInitialFootPositionY(round(math.cos(math.radians(self._COXA_ANGLE))*(self._LENGTH_COXA + self._LENGTH_FEMUR + self._initLegStretch)))
        leg_right_rear.setInitialFootPositionZ(self._LENGTH_TIBIA + self._rideHeightOffset)
        leg_right_rear.setLegBasePositionX = -self._X_COXA
        leg_right_rear.setLegBasePositionY = -self._Y_COXA_FB
        leg_right_rear.setLegBasePositionZ = 0
        self.legs.append(leg_right_rear)

    def BodyIK(self, x, y, z):
        bodyRotOffsetX = []
        bodyRotOffsetY = []
        bodyRotOffsetZ = []

        globalInitFootPosX = None
        globalInitFootPosY = None
        globalInitFootPosZ = None

        sinRotX = math.sin(math.radians(x))
        cosRotX = math.cos(math.radians(x))
        sinRotY = math.sin(math.radians(y))
        cosRotY = math.cos(math.radians(y))
        sinRotZ = math.sin(math.radians(z))
        cosRotZ = math.cos(math.radians(z))

        legs = []

        for i in range(0, 5):
            globalInitFootPosX = Leg(i).setInitialFootPosition()
