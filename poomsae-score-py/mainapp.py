import score
import fullscore
import competitor
import division

from tkinter import *

if __name__ == '__main__':
    root = Tk()
    
    score_frame = Frame(root, width=800, height=600)
    
    judge_0 = Label(score_frame, text='0.00', fg='yellow', bg='black')
    judge_1 = Label(score_frame, text='0.00', fg='yellow', bg='black')
    judge_2 = Label(score_frame, text='0.00', fg='yellow', bg='black')
    judge_3 = Label(score_frame, text='0.00', fg='yellow', bg='black')
    judge_4 = Label(score_frame, text='0.00', fg='yellow', bg='black')
    
    judge_0.pack(side=LEFT)
    judge_1.pack(side=LEFT)
    judge_2.pack(side=LEFT)
    judge_3.pack(side=LEFT)
    judge_4.pack(side=LEFT)

    
    score_frame.pack()
    
    root.mainloop()
    
