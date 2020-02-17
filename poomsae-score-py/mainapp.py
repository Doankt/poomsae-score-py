import wx
from collections import namedtuple
import time
# import score
# import fullscore
# import competitor
# import division
from controllers import controller
from frames.menu_frame import MenuFrame

class MainHandler(wx.App):
    def __init__(self):
        self.app = super().__init__()
        self.menu = MenuFrame()
        self.menu.Show()


if __name__ == '__main__':
    app = MainHandler()
    # frame = MenuFrame()

    # ard1 = controller.Controller('COM8')
    # ard1.start()
    # while True:
    #     print(ard1.score)
    #     time.sleep(1)

    app.MainLoop()
