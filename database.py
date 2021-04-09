import sqlite3


def execute(query):
    
     
    conn =  sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(query)  
    conn.commit()
    conn.close()

 