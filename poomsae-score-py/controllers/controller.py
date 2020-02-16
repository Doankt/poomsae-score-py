from serial import *
import time
import threading

CONTROLLER_TIMEOUT = 12

def _read_thread(controller):
    last_ping = time.time()
    while True:
        try:
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
                raise SerialException()
            time.sleep(0.5)

        except SerialException:
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
    print("eot")


class Controller():

    def __init__(self, port):
        self.ser = Serial(port, baudrate=9600, timeout=5)
        self.score = []
        self.read_thread = None


    def start(self):
        self.read_thread = threading.Thread(target=_read_thread, args=(self,))
        self.read_thread.daemon = True
        self.read_thread.start()

    def attempt_reconnect(self, p, b, t):
        self.ser.close()
        self.ser = Serial(p, baudrate=b, timeout=t)


    def _ping(self):
        pass


