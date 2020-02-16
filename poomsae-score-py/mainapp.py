import wx
from collections import namedtuple

# import model.score
# import model.fullscore
# import model.competitor
# import model.division

from frames.menu_frame import MenuFrame


if __name__ == '__main__':
    app = wx.App()
    frame = MenuFrame()
    # frame = MenuFrame()
    app.MainLoop()
