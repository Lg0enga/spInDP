from dxl.dxlchain import DxlChain

# Open the serial device
chain = DxlChain("/dev/ttyAMA0", rate=1000000)

speed = 1

chain.goto(10, 512, speed=int(512 * speed))
chain.goto(11, 355, speed=int(245 * speed))
chain.goto(12, 110, speed=int(511 * speed))

chain.goto(10, 665, speed=int(512 * speed))
chain.goto(11, 428, speed=int(245 * speed))
chain.goto(12, 263, speed=int(511 * speed))

chain.goto(11, 467, speed=int(512 * speed))
chain.goto(12, 291, speed=int(371 * speed))

chain.goto(10, 512, speed=int(512 * speed))
chain.goto(11, 404, speed=int(209 * speed))
chain.goto(12, 138, speed=int(509 * speed))

chain.goto(10, 358, speed=int(512 * speed))
chain.goto(11, 467, speed=int(209 * speed))
chain.goto(12, 291, speed=int(509 * speed))

chain.goto(11, 428, speed=int(512 * speed))
chain.goto(12, 263, speed=int(371 * speed))

chain.disable()
