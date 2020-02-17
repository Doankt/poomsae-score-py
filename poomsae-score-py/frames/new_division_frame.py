import wx

class NewDivisionFrame(wx.Frame):
    def __init__(self, menu_frame):
        super().__init__(menu_frame, title="New Division")
        self._parent = menu_frame

        panel = wx.Panel(self)
        fgs = wx.FlexGridSizer(2, 2, 50, 50)
        hbox = wx.BoxSizer(wx.HORIZONTAL)


        fgs.Add(wx.StaticText(panel, label="test"))
        fgs.Add(wx.TextCtrl(panel))
        fgs.Add(wx.StaticText(panel, label="test2"))


        hbox.Add(fgs, border=15)
        panel.SetSizer(hbox)
        panel.Show()


        self.Bind(wx.EVT_CLOSE, self._frame_close)


    def _frame_close(self, event):
        self._parent.Enable()
        self.Destroy()
