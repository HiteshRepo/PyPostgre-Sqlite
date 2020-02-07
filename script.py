# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 02:49:15 2020

@author: Hitesh Pattanayak
"""

import sqlite3

def create_table():
    try:
        conn = sqlite3.connect("lite.db")
        cur=conn.cursor()
        cur.execute("CREATE TABLE Store (item TEXT, quantity INTEGER, price REAL)")
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
    
def insert_table(item, qty, price):
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO Store VALUES(?, ?, ?)",(item, qty, price))
    conn.commit()
    conn.close()
    
def view():
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM Store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(qty,price,item):
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE Store SET quantity = ?, price = ? WHERE item=?",(qty,price,item))
    conn.commit()
    conn.close()
    
create_table()
insert_table('water', 10, 10.5)
insert_table('coffee cup', 8, 12.5)
delete('water')
update(10, 15, 'coffee cup')
print(view())