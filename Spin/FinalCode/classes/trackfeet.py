import dynamixel

class TrackFeet:

    serial = dynamixel.SerialStream(port="/dev/USB2AX",
                                    baudrate="1000000",
                                    timeout=1)

    net = dynamixel.DynamixelNetwork(serial)

    servos = [32, 40, 41, 10, 11, 12, 61, 50, 51, 20, 21, 22, 62, 52, 60, 42, 30, 31]

    for servoId in servos:
        newDynamixel = dynamixel.Dynamixel(servoId, net)
        net._dynamixel_map[servoId] = newDynamixel

    def track(self):
        while True:
            self.net._dynamixel_map[40].goal_position = self.net._dynamixel_map[60].current_position
            self.net._dynamixel_map[40].moving_speed = 1023
            self.net._dynamixel_map[41].goal_position = self.net._dynamixel_map[61].current_position
            self.net._dynamixel_map[41].moving_speed = 1023
            self.net._dynamixel_map[42].goal_position = self.net._dynamixel_map[62].current_position
            self.net._dynamixel_map[42].moving_speed = 1023
            self.net._dynamixel_map[50].goal_position = self.net._dynamixel_map[60].current_position
            self.net._dynamixel_map[50].moving_speed = 1023
            self.net._dynamixel_map[51].goal_position = self.net._dynamixel_map[61].current_position
            self.net._dynamixel_map[51].moving_speed = 1023
            self.net._dynamixel_map[52].goal_position = self.net._dynamixel_map[62].current_position
            self.net._dynamixel_map[52].moving_speed = 1023
            self.net.synchronize()

if __name__ == '__main__':
    main = TrackFeet()
    main.track()
