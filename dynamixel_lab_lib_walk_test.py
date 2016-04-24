from dxl.dxlchain import DxlChain

__author__ = 'Jelmer Visser'

# Open the serial device
chain = DxlChain("/dev/ttyAMA0", rate=1000000)

speed = 1


def degreesToBits(degrees):
    return (1023 * degrees) / 300


def walk():
    chain.goto(10, degreesToBits(150), speed=int(512 * speed))
    chain.goto(11, degreesToBits(104), speed=int(245 * speed))
    chain.goto(12, degreesToBits(32.2), speed=int(511 * speed))

    chain.goto(10, degreesToBits(195), speed=int(512 * speed))
    chain.goto(11, degreesToBits(125.6), speed=int(245 * speed))
    chain.goto(12, degreesToBits(77.1), speed=int(511 * speed))

    chain.goto(11, degreesToBits(137), speed=int(512 * speed))
    chain.goto(12, degreesToBits(85.4), speed=int(371 * speed))

    chain.goto(10, degreesToBits(150), speed=int(512 * speed))
    chain.goto(11, degreesToBits(118.6), speed=int(209 * speed))
    chain.goto(12, degreesToBits(40.6), speed=int(509 * speed))

    chain.goto(10, degreesToBits(105), speed=int(512 * speed))
    chain.goto(11, degreesToBits(137), speed=int(209 * speed))
    chain.goto(12, degreesToBits(85.4), speed=int(509 * speed))

    chain.goto(11, degreesToBits(125.6), speed=int(512 * speed))
    chain.goto(12, degreesToBits(77.1), speed=int(371 * speed))

    chain.disable()


def main():
    walk()

if __name__ == '__main__':
    main()
