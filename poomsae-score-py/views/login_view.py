import tkinter as tk

class LoginTopLevel(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.master = master
        self._window_config()
        self._current_frame = None
        self.swap_frame(SignInFrame)

    def _window_config(self):
        self.title('Account')
        self.config(bg='blue')
        self.protocol("WM_DELETE_WINDOW", self.destroy)

    def swap_frame(self, frame_class):
        temp_frame = frame_class(self)

        if self._current_frame:
            self._current_frame.destroy()

        self._current_frame = temp_frame
        self._current_frame.pack()


class SignInFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self._frame_config()
        self._frame_create()

    def _frame_config(self):
        self.config(bg='yellow', width=400, height=300)

    def _frame_create(self):
        tk.Label(self, text='Sign in').grid(row=0, column=0)
        tk.Label(self, text='Username').grid(row=1, column=0)
        tk.Label(self, text='Password').grid(row=2, column=0)

        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=1, column=1)
        self.password_entry = tk.Entry(self)
        self.password_entry.grid(row=2, column=1)

        tk.Button(self, text='NEXT', command=lambda :self.master.swap_frame(SignUpFrame)).grid(row=3, column=0)


class SignUpFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self._frame_config()
        self._frame_create()

    def _frame_config(self):
        self.config(bg='yellow', width=400, height=300)

    def _frame_create(self):
        tk.Label(self, text='S O').pack()


class AccountResultFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self._frame_config()
        self._frame_create()

    def _frame_config(self):
        self.config(bg='yellow')

    def _frame_create(self):
        pass