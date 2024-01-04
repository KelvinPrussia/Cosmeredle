import sqlite3
import json

def get_names():
    conn = sqlite3.connect('database/cosmeredle.db')
    res = conn.execute("SELECT name FROM character_list").fetchall()

    res_list = []
    for tup in res:
        res_list.append(tup[0])

    conn.close()
    return res_list

def get_character_data(name):
    conn = sqlite3.connect('database/cosmeredle.db')
    res = conn.execute(f"SELECT * FROM character_data WHERE name = {name}").fetchone()

    conn.close()
    return res

def get_columns():
    conn = sqlite3.connect('database/cosmeredle.db')
    columns = conn.execute("SELECT name FROM pragma_table_info('character_data')").fetchall()

    column_list = []
    for tup in columns:
        column_list.append(tup[0])

    conn.close()
    return column_list