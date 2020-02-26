import sys
sys.path.append('..')

from serial import *
import time
import threading
from scoring.score import Score
import controllers.controller_exceptions

ACC_CHAR = b'!'
PRES_CHAR = b'@'
PING_CHAR = b'#'
SCORE_RESET_CHAR = b'$'
END_CHAR = b'~'


CONTROLLER_TIMEOUT = 10

class ControllerDisconnectException(Exception):
    def __init__(self, port):
        super().__init__(self)
        self.message = "{} controller disconnected".format(port)

    def __str__(self):
        return self.message

class Controller:
    def __init__(self, port, mainapp, slotnum):
        self.ser = Serial(port, baudrate=9600, timeout=5)
        self.score = Score()
        self.read_thread = None
        self.continue_read_thread = False
        self.mainapp = mainapp
        self.slot_num = slotnum

        self.mainapp.controller_list[self.slot_num] = self

    def _read_thread(self):
        last_ping = time.time()
        while self.continue_read_thread:
            try:
                data = self.ser.read(1)
                print(self.score.total_avg())
                if data == ACC_CHAR or data == PRES_CHAR:
                    #Recieving Score
                    sec = data
                    string = ""
                    while True:
                        data = self.ser.read(1)
                        if data == END_CHAR: break
                        string += data.decode('utf-8')

                    if sec == ACC_CHAR:    self.score.accuracy = float(string)
                    else:   self.score.presentation = float(string)
                elif data == SCORE_RESET_CHAR:
                    self.score = Score()
                elif data == PING_CHAR:
                    last_ping = time.time()

                if ((time.time() - last_ping) >= CONTROLLER_TIMEOUT):
                    raise ControllerDisconnectException(self.ser.port)

            except:
                print("Controller {} Disconnected".format(self.ser.port))
                retry = 0

                port = self.ser.port
                baud = self.ser.baudrate
                timeo = self.ser.timeout

                while retry < 3:
                    print("retry:", retry)
                    try:
                        self.attempt_reconnect(port, baud, timeo)
                        if self.ser.read(1) == PING_CHAR:
                            break
                    finally:
                        retry += 1
                        time.sleep(5)

                if retry >= 3:
                    print("controller failed to reconnect")
                    break
                print("Controller {} Reconnected".format(self.ser.port))

    def start(self):
        if not self.read_thread:
            self.read_thread = threading.Thread(target=self._read_thread)
            self.read_thread.daemon = True
            self.continue_read_thread = True
            self.read_thread.start()

    def attempt_reconnect(self, p, b, t):
        self.ser.close()
        self.ser = Serial(p, baudrate=b, timeout=t)

    def stop(self):
        self.continue_read_thread = False
        self.read_thread = None
        self.__del__()

    def __del__(self):
        self.continue_read_thread = False
        self.ser.close()
        self.read_thread = None
        self.mainapp.controller_list[self.slot_num] = None
