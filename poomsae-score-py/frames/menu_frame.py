import wx
import frames.menu_bar
import frames.new_division_frame


class MenuFrame(wx.Frame):
    def __init__(self, par=None):
        super().__init__(par, title="Menu")

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        new_div_button = wx.Button(panel, label="NEW")
        new_div_button.Bind(wx.EVT_BUTTON, self.open_new)

        open_div_button = wx.Button(panel, label="OPEN")

        sizer.Add(new_div_button, 0, wx.ALL | wx.EXPAND, 10)
        sizer.Add(open_div_button, 0, wx.ALL | wx.EXPAND, 10)

        panel.SetSizer(sizer)

        mf = frames.menu_bar.MainMenuBar()
        self.SetMenuBar(mf)

        self.Show()

    def open_new(self, event):
        nd = frames.new_division_frame.NewDivisionFrame(self)
        self.Disable()
        nd.Show()
        

