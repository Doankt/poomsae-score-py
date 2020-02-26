import sqlite3 as sql
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def create_division(type: int, belt: str, age: str):
    # save_dir = filedialog.askdirectory()
    # print(save_dir)
    connection = sql.connect('new.db')
    cur = connection.cursor()

    with open(filedialog.askopenfilename()) as file:
        cur.executescript(file.read())
    connection.commit()
    connection.close()
