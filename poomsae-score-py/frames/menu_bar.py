import wx


class MainMenuBar(wx.MenuBar):
    def __init__(self, style=0):
        super().__init__(style)

        #File
        mu = wx.Menu()
        mu.Append(wx.ID_ABOUT, "aa", "descrip")
        self.Append(mu, "file")

        #Controller
        mu = wx.Menu()
        mu.Append(wx.ID_ANY, "connect", "conts here")
        self.Append(mu, "CONTROLLERS")



