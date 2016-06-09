from flask import Flask
import dynamixel
import json

app = Flask(__name__)

serial = dynamixel.SerialStream(port="/dev/USB2AX",
                                baudrate="1000000",
                                timeout=1)

net = dynamixel.DynamixelNetwork(serial)

servos = [32, 40, 41, 10, 11, 12, 61, 50, 51, 20, 21, 22, 62, 52, 60, 42, 30, 31]

staHoogte = 0

for servoId in servos:
    newDynamixel = dynamixel.Dynamixel(servoId, net)
    net._dynamixel_map[servoId] = newDynamixel

@app.route('/')
def index():

    data = {'battery_percentage': 80, 'spider_angle': 20, 'legs': [{
        'servos': [{
            'id': 10,
            'temperature': net._dynamixel_map[10].current_temperature,
            'voltage': net._dynamixel_map[10].current_voltage,
            'force': net._dynamixel_map[10].current_load,
            'position': net._dynamixel_map[10].current_speed,
            'torque': net._dynamixel_map[10].torque_limit
        },
        {
            'id': 11,
            'temperature': net._dynamixel_map[11].current_temperature,
            'voltage': net._dynamixel_map[11].current_voltage,
            'force': net._dynamixel_map[11].current_load,
            'position': net._dynamixel_map[11].current_speed,
            'torque': net._dynamixel_map[11].torque_limit
        },
        {
            'id': 12,
            'temperature': net._dynamixel_map[12].current_temperature,
            'voltage': net._dynamixel_map[12].current_voltage,
            'force': net._dynamixel_map[12].current_load,
            'position': net._dynamixel_map[12].current_speed,
            'torque': net._dynamixel_map[12].torque_limit
        }]
    },
    {
        'servos': [{
            'id': 20,
            'temperature': net._dynamixel_map[20].current_temperature,
            'voltage': net._dynamixel_map[20].current_voltage,
            'force': net._dynamixel_map[20].current_load,
            'position': net._dynamixel_map[20].current_speed,
            'torque': net._dynamixel_map[20].torque_limit
        },
        {
            'id': 21,
            'temperature': net._dynamixel_map[21].current_temperature,
            'voltage': net._dynamixel_map[21].current_voltage,
            'force': net._dynamixel_map[21].current_load,
            'position': net._dynamixel_map[21].current_speed,
            'torque': net._dynamixel_map[21].torque_limit
        },
        {
            'id': 22,
            'temperature': net._dynamixel_map[22].current_temperature,
            'voltage': net._dynamixel_map[22].current_voltage,
            'force': net._dynamixel_map[22].current_load,
            'position': net._dynamixel_map[22].current_speed,
            'torque': net._dynamixel_map[22].torque_limit
        }]
    },
    {
        'servos': [{
            'id': 30,
            'temperature': net._dynamixel_map[30].current_temperature,
            'voltage': net._dynamixel_map[30].current_voltage,
            'force': net._dynamixel_map[30].current_load,
            'position': net._dynamixel_map[30].current_speed,
            'torque': net._dynamixel_map[30].torque_limit
        },
        {
            'id': 31,
            'temperature': net._dynamixel_map[31].current_temperature,
            'voltage': net._dynamixel_map[31].current_voltage,
            'force': net._dynamixel_map[31].current_load,
            'position': net._dynamixel_map[31].current_speed,
            'torque': net._dynamixel_map[31].torque_limit
        },
        {
            'id': 32,
            'temperature': net._dynamixel_map[32].current_temperature,
            'voltage': net._dynamixel_map[32].current_voltage,
            'force': net._dynamixel_map[32].current_load,
            'position': net._dynamixel_map[32].current_speed,
            'torque': net._dynamixel_map[32].torque_limit
        }]
    },
    {
        'servos': [{
            'id': 40,
            'temperature': net._dynamixel_map[40].current_temperature,
            'voltage': net._dynamixel_map[40].current_voltage,
            'force': net._dynamixel_map[40].current_load,
            'position': net._dynamixel_map[40].current_speed,
            'torque': net._dynamixel_map[40].torque_limit
        },
        {
            'id': 41,
            'temperature': net._dynamixel_map[41].current_temperature,
            'voltage': net._dynamixel_map[41].current_voltage,
            'force': net._dynamixel_map[41].current_load,
            'position': net._dynamixel_map[41].current_speed,
            'torque': net._dynamixel_map[41].torque_limit
        },
        {
            'id': 42,
            'temperature': net._dynamixel_map[42].current_temperature,
            'voltage': net._dynamixel_map[42].current_voltage,
            'force': net._dynamixel_map[42].current_load,
            'position': net._dynamixel_map[42].current_speed,
            'torque': net._dynamixel_map[42].torque_limit
        }]
    },
    {
        'servos': [{
            'id': 50,
            'temperature': net._dynamixel_map[50].current_temperature,
            'voltage': net._dynamixel_map[50].current_voltage,
            'force': net._dynamixel_map[50].current_load,
            'position': net._dynamixel_map[50].current_speed,
            'torque': net._dynamixel_map[50].torque_limit
        },
        {
            'id': 51,
            'temperature': net._dynamixel_map[51].current_temperature,
            'voltage': net._dynamixel_map[51].current_voltage,
            'force': net._dynamixel_map[51].current_load,
            'position': net._dynamixel_map[51].current_speed,
            'torque': net._dynamixel_map[51].torque_limit
        },
        {
            'id': 52,
            'temperature': net._dynamixel_map[52].current_temperature,
            'voltage': net._dynamixel_map[52].current_voltage,
            'force': net._dynamixel_map[52].current_load,
            'position': net._dynamixel_map[52].current_speed,
            'torque': net._dynamixel_map[52].torque_limit
        }]
    },
    {
        'servos': [{
            'id': 60,
            'temperature': net._dynamixel_map[60].current_temperature,
            'voltage': net._dynamixel_map[60].current_voltage,
            'force': net._dynamixel_map[60].current_load,
            'position': net._dynamixel_map[60].current_speed,
            'torque': net._dynamixel_map[60].torque_limit
        },
        {
            'id': 61,
            'temperature': net._dynamixel_map[61].current_temperature,
            'voltage': net._dynamixel_map[61].current_voltage,
            'force': net._dynamixel_map[61].current_load,
            'position': net._dynamixel_map[61].current_speed,
            'torque': net._dynamixel_map[61].torque_limit
        },
        {
            'id': 62,
            'temperature': net._dynamixel_map[62].current_temperature,
            'voltage': net._dynamixel_map[62].current_voltage,
            'force': net._dynamixel_map[62].current_load,
            'position': net._dynamixel_map[62].current_speed,
            'torque': net._dynamixel_map[62].torque_limit
        }]
    }]}

    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
