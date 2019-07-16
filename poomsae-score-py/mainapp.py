import tkinter as tk
from tkinter.filedialog import askopenfilename
import tkinter.ttk as ttk

from collections import namedtuple

import score
import fullscore
import competitor
import division
from audience_view import AudienceTopLevel
from admin_view import AdminTopLevel

# Controller
class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        self.admin_view = AdminTopLevel(self)
        self._define_buttons()

    def _define_buttons(self):
        # Admin View
        admin_frame = self.admin_view.admin_frame

        admin_frame.aud_view_button.bind('<Button-1>', self._show_audience_view)
        admin_frame.open_division_button.bind('<Button-1>', self._make_divison)

    def _make_divison(self, event):
        file = askopenfilename(initialdir='.',
                               filetypes=[('Poomsae Score Divison', '.psdiv')])
        print(file)

    def _show_audience_view(self, event):
        self.audience_view = AudienceTopLevel(self)

    def _randomscore(self, event):
        print(event.widget)
        event.widget.config(text=score.gen_random_score())

if __name__ == '__main__':
    root = MainApp()
    root.mainloop()
