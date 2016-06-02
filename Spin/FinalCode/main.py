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
        self._Mode = ""

        p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        self.out, err = p.communicate()

    def CommandHandler(self):
        while not self._Exit:
            data = self._Buffer.Pop()

            if len(str(data)) > 0:
                if "exit" in data:
                    self._Handler.StopWalk()
                    self.Exit()
                    self._Exit = True
                    self._Mode = ""
                    #exit()
                else:
                    print data

                    if "NormalWalk" in data:
                        self._Mode = "NormalWalk"
                    elif "prik" in data:
                        self._Mode = "Prik"

                    if self._Mode == "Prik":
                        self._Handler.StopWalk()
                        self._Handler.set_speed(0, 400)
                        self._Handler.prik()
                        self._Mode = ""

                    if self._Mode == "NormalWalk":
                        self._Handler.StartWalk()
                        data = data.replace("walk", "")

                        try:
                            data_arr = cPickle.loads(data)

                            x = int(data_arr[0])
                            y = int(data_arr[1])

                            #self._Handler.BodyIK(x, y)

                            if y > 100.0 or y < -100.0:
                                self._Handler.set_speed(0, y)
                            else:
                                self._Handler.set_speed(x, 0)
                            print("NormalWalk Activated")

                        except cPickle.UnpicklingError:
                            self._Handler.set_speed(1023, 1023)
                            print("DATA ERROR")

                    # Krab walk
                    if "KrabWalk" in data:

                        data = data.replace("KrabWalk", "")

                        try:
                            data_arr = cPickle.loads(data)

                            x = int(data_arr[0])
                            y = int(data_arr[1])

                            #self._Handler.BodyIK(x, y)

                            #if y > 100.0 or y < -100.0:
                            #    self._Handler.set_speed(0, y)
                            #else:
                            #    self._Handler.set_speed(x, 0)
                            print("KrabWalk Activated")

                        except cPickle.UnpicklingError:
                            self._Handler.set_speed(1023, 1023)
                            print("DATA ERROR")

                    #print(data)

    def Exit(self):
        self._Server.Exit()
        self._Handler.Exit()
        print("Goodbye")


if __name__ == '__main__':
    main = Main()
