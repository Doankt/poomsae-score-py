import tkinter as tk
import tkinter.ttk as ttk

from collections import namedtuple
import score

# View window
class AudienceTopLevel(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.master = master
        self._window_config()
        self._window_create()

    def _window_config(self):
        self.title('Audience View')
        self.config(bg='orange')
        self.protocol("WM_DELETE_WINDOW", self.withdraw)

    def _window_create(self):
        self.current_score_frame = AudienceCurrentScoreFrame(self)
        self.current_score_frame.pack()

# View frame
class AudienceCurrentScoreFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self._frame_config()
        self._frame_create()

    def _frame_config(self):
        pass

    def _frame_create(self):
        self.score_frame = tk.Frame(self)
        score_pack = namedtuple('ScorePack', ['accuracy_label', 'presentation_label'])
        self.score_list = []
        for i in range(5):
            self.score_list.append(
                score_pack(tk.Label(self.score_frame, text='0.00', fg='yellow', bg='black', font=('ariel', 30)),
                           tk.Label(self.score_frame, text='0.00', fg='yellow', bg='black', font=('ariel', 30))))
            self.score_list[i].accuracy_label.grid(padx=(20, 0), row=0, column=i)
            self.score_list[i].accuracy_label.bind('<Button-1>', self._randomscore)
            self.score_list[i].presentation_label.grid(padx=(20, 0), row=1, column=i)

        self.score_frame.pack()

    # Delete later as audience should not be able to interact with anything
    def _randomscore(self, event):
        print(event.widget)
        event.widget.config(text=score.gen_random_score())

