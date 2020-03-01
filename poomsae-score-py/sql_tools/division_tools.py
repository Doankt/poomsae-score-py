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

def get_division_info(conn):
    cur = conn.cursor()

    cur.execute('''
                    SELECT *
                    FROM DivisionInfo
                ''')
    return cur.fetchone()

def get_next_round(conn):
    #-1 division complete
    #-2 no entries
    cur = conn.cursor()

    cur.execute('''
                    SELECT r_id
                    FROM Rounds
                    WHERE comp_flag != 1
                    ORDER BY r_id
                ''')

    data = cur.fetchone()
    if data is not None:
        return data[0]
    else:
        cur.execute('''
                        SELECT COUNT(*)
                        FROM Rounds
                    ''')
        if cur.fetchone()[0] > 0:
            return -1
        return -2

test = sql.connect(r'D:\System Locations\Documents\GitHub\poomsae-score-py\Design Files\framework.db')
print(get_division_info(test))
print(get_next_round(test))