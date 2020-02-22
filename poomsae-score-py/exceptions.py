class StopControllerException(Exception):
    def __init__(self, port):
        super().__init__(self)
        self.message = "{} controller stopped".format(port)

    def __str__(self):
        return self.message