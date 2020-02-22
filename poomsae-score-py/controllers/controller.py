from serial import *
import time
import threading
import controllers.controller_exceptions

CONTROLLER_TIMEOUT = 10

class ControllerDisconnectException(Exception):
    def __init__(self, port):
        super().__init__(self)
        self.message = "{} controller disconnected".format(port)

    def __str__(self):
        return self.message

def _read_thread(controller):
    last_ping = time.time()
    while True:
        try:
            if controller.stop_flag:
                break

            data = controller.ser.read(1)
            if data == b'<':
                string = ""
                while True:
                    data = controller.ser.read(1)
                    if data == b'>': break
                    string += data.decode('utf-8')
                controller.score = [float(n) for n in string.split(',')]
            elif data == b'#':
                print("pinged")
                last_ping = time.time()

            if((time.time() - last_ping) >= CONTROLLER_TIMEOUT):
                raise ControllerDisconnectException(controller.ser.port)
            time.sleep(0.5)

        except ControllerDisconnectException:
            print("Controller Disconnected")
            retry = 0

            port = controller.ser.port
            baud = controller.ser.baudrate
            timeo = controller.ser.timeout

            while retry < 3:
                print("retry:", retry)
                try:
                    controller.attempt_reconnect(port, baud, timeo)
                    break
                except:
                    retry += 1
                    time.sleep(5)
            if retry >= 3:
                print("controller failed to reconnect")
                break
            print("controller reconnected")
    print("eot")


class Controller:

    def __init__(self, port):
        self.ser = Serial(port, baudrate=9600, timeout=5)
        self.score = []
        self.read_thread = None
        self.stop_flag = -1

    def start(self):
        if not self.read_thread:
            self.read_thread = threading.Thread(target=_read_thread, args=(self,))
            self.read_thread.daemon = True
            self.stop_flag = 0
            self.read_thread.start()

    def attempt_reconnect(self, p, b, t):
        self.ser.close()
        self.ser = Serial(p, baudrate=b, timeout=t)

    def stop(self):
        self.stop_flag = 1
        self.read_thread = None
