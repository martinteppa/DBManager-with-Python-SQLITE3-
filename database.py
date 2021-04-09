import sqlite3


def exxecute(query):
    
     
    conn =  sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(query)  
    conn.commit()
    conn.close()


def buscar(query):
    conn =  sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(query) 
    value = c.fetchall() 
    conn.commit()
    conn.close()
    return value