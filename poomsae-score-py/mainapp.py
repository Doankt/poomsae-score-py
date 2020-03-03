import wx
from collections import namedtuple
import time
# import score
# import fullscore
# import competitor
# import division
from controllers import controller

class MainHandler(wx.App):
    def __init__(self):
        self.app = super().__init__()
        self.menu = MenuFrame()
        self.menu.Show()


if __name__ == '__main__':
    # app = MainHandler()
    # frame = MenuFrame()

    ard1 = controller.Controller('COM6')
    ard1.start()
    while True:
        print(ard1.score.total_avg())
        time.sleep(1)
        # ard1.stop()

    # app.MainLoop()
