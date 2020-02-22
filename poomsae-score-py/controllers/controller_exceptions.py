class ControllerDisconnectException(Exception):
    def __init__(self, port):
        super().__init__(self)
        self.message = "{} controller disconnected".format(port)

    def __str__(self):
        return self.message