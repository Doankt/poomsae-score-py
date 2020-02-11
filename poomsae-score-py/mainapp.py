import wx
from collections import namedtuple

# import model.score
# import model.fullscore
# import model.competitor
# import model.division

import model

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(parent=None, title="test")
    frame.Show()
    app.MainLoop()
