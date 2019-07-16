import tkinter as tk

from audience_view import AudienceTopLevel

# View window
class AdminTopLevel(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.master = master
        self._window_config()
        self._window_create()

    def _window_config(self):
        self.title('Admin View')
        self.config(bg='white')
        self.protocol("WM_DELETE_WINDOW", self.master.destroy)

    def _window_create(self):
        self.admin_frame = AdminFrame(self)
        self.admin_frame.pack()

# View frame
class AdminFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self._frame_config()
        self._frame_create()

    def _frame_config(self):
        self.config(bg='blue', width=800, height=600)
        self.pack_propagate(False)

    def _frame_create(self):
        self.lab = tk.Label(self, text='LAAAAAAAAABEL')
        self.lab.pack()

        self.aud_view_button = tk.Button(self, text='Show Audience View')
        self.aud_view_button.pack(side=tk.BOTTOM)

        self.open_division_button = tk.Button(self, text='Open division')
        self.open_division_button.pack()
