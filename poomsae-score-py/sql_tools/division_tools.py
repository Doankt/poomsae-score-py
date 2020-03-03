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

def add_score(conn, r_id, c_id, j_num:int, acc:float, pres_list:[float]):
    cur = conn.cursor()

    cur.execute('''
                    INSERT INTO Scores
                    VALUES ({}, {}, {}, {}, {}, {}, {})
                '''.format(r_id, c_id, j_num, acc, pres_list[0], pres_list[1], pres_list[2]))

    conn.commit()

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

def get_round_comp_time(conn):
    cur = conn.cursor()
    r = get_next_round(conn)

    cur.execute('''
                    SELECT comp_time
                    FROM Rounds
                    WHERE r_id = {}
                '''.format(r))

    return cur.fetchone()[0]
