import sqlite3

def create_db():
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS PURCHASE (
                    purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Land_Type TEXT,
                    Area_SQ TEXT,
                    Purchaser_Name TEXT,
                    location TEXT,
                    Area_Type TEXT,
                    Upper_Price TEXT,
                    Lower_Price TEXT,
                    User_Type TEXT,
                    Address TEXT,
                    Contact TEXT
                )''')
    con.commit()
    
    cur.execute('''CREATE TABLE IF NOT EXISTS RENT (
                    rent_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Land_Type TEXT,
                    Area_SQ TEXT,
                    Name TEXT,
                    location TEXT,
                    Area_Type TEXT,
                    Upper_Price TEXT,
                    Lower_Price TEXT,
                    User_Type TEXT,
                    Address TEXT,
                    Contact TEXT
                )''')
    con.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS SELL(
                    sell_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Land_Type TEXT,
                    Area_SQ TEXT,
                    Name TEXT,
                    location TEXT,
                    Area_Type TEXT,
                    Upper_Price TEXT,
                    Lower_Price TEXT,
                    User_Type TEXT,
                    Address TEXT,
                    Contact TEXT
                )''')
    con.commit()
    
    
create_db()
