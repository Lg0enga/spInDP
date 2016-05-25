from classes.buffer import Buffer
from classes.server import Server
from classes.handler import Handler
import time
import threading
import subprocess
import cPickle
import sys
import subprocess, signal

class Main(object):
    def __init__(self):
        self._Buffer = Buffer()
        self._Server = Server(self._Buffer)
        self._Handler = Handler(1)
        self._Exit = False

        self._ServerThread = threading.Thread(target=self._Server.Start)
        self._ServerThread.start()
        self._CommandHandlerThread = threading.Thread(target=self.CommandHandler)
        self._CommandHandlerThread.start()
        self._HandlerThread = threading.Thread(target=self._Handler.runThread)
        self._HandlerThread.start()

        p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        self.out, err = p.communicate()

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

                        try:
                            data_arr = cPickle.loads(data)

                            x = int(data_arr[0])
                            y = int(data_arr[1])

                            if y > 100.0 or y < -100.0:
                                self._Handler.set_speed(0, y)
                            else:
                                self._Handler.set_speed(x, 0)
                                print "rust stand"

                        except cPickle.UnpicklingError:
                            self._Handler.set_speed(10, 10)
                            print "DATA ERROR"

                    print data

    def Exit(self):
        self._Server.Exit()
        self._Handler.Exit()
        print "Goodbye"


if __name__ == '__main__':
    main = Main()
