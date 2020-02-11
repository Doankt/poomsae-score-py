import wx


class MenuFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Menu")

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        new_div_button = wx.Button(panel, label="NEW")
        new_div_button.Bind(wx.EVT_BUTTON, self.open_new)

        open_div_button = wx.Button(panel, label="OPEN")

        sizer.Add(new_div_button, 0, wx.ALL | wx.EXPAND, 10)
        sizer.Add(open_div_button, 0, wx.ALL | wx.EXPAND, 10)

        panel.SetSizer(sizer)

        self.Show()

    def open_new(self, event):
        print(event)
        

