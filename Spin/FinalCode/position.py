import dynamixel

serial = dynamixel.SerialStream(port="/dev/USB2AX",
                                baudrate="1000000",
                                timeout=1)

net = dynamixel.DynamixelNetwork(serial)

servos = [32, 40, 41, 10, 11, 12, 61, 50, 51, 20, 21, 22, 62, 52, 60, 42, 30, 31]

for servoId in servos:
    newDynamixel = dynamixel.Dynamixel(servoId, net)
    net._dynamixel_map[servoId] = newDynamixel

print str(net._dynamixel_map[10].current_position) + ";" + str(net._dynamixel_map[11].current_position) + ";" + str(net._dynamixel_map[12].current_position) + ";" + str(net._dynamixel_map[20].current_position) + ";" + str(net._dynamixel_map[21].current_position) + ";" + str(net._dynamixel_map[22].current_position) + ";" + str(net._dynamixel_map[30].current_position) + ";" + str(net._dynamixel_map[31].current_position) + ";" + str(net._dynamixel_map[32].current_position) + ";" + str(net._dynamixel_map[40].current_position) + ";" + str(net._dynamixel_map[41].current_position) + ";" + str(net._dynamixel_map[42].current_position) + ";" + str(net._dynamixel_map[50].current_position) + ";" + str(net._dynamixel_map[51].current_position) + ";" + str(net._dynamixel_map[52].current_position) + ";" + str(net._dynamixel_map[60].current_position) + ";" + str(net._dynamixel_map[61].current_position) + ";" + str(net._dynamixel_map[62].current_position)
