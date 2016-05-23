from classes.buffer import Buffer
from classes.server import Server
from classes.walk import Walk
import time
import threading
import subprocess
import cPickle
import sys

class Main(object):
    def __init__(self):
        self._Buffer = Buffer()
        self._Server = Server(self._Buffer)
        self._Walk = Walk()
        self._Exit = False

        self._ServerThread = threading.Thread(target=self._Server.Start)
        self._ServerThread.deamon = True
        self._ServerThread.start()
        self._CommandHandlerThread = threading.Thread(target=self.CommandHandler)
        self._CommandHandlerThread.deamon = True
        self._CommandHandlerThread.start()
        self._HandlerThread = threading.Thread(target=self._Walk.walk)
        self._HandlerThread.deamon = True
        self._HandlerThread.start()

    def CommandHandler(self):
        while not self._Exit:
            data = self._Buffer.Pop()

            if len(str(data)) > 0:
                if "exit" in data:
                    self.Exit()
                    self._Exit = True
                    exit()
                else:
                    if "walk" in data:
                        data = data.replace("walk", "")
                        data_arr = cPickle.loads(data)

                        x = int(data_arr[0])
                        y = int(data_arr[1])

                        print data

                        # x = int(data_arr[0])
                        # y = int(data_arr[1])
                        #
                        # if y < 1023 and y > -1023:
                        #     if y > 100:
                        #         self._Walk.set_speed(0, y)
                        #     else:
                        #         self._Walk.stop()
                        # else:
                        #     self._Walk.stop()

                    print data

    def Exit(self):
        sys.exit(0)


if __name__ == '__main__':
    main = Main()
