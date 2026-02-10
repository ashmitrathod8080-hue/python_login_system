import sqlite3
import hashlib

conn = sqlite3.connect('sample.db')
c = conn.cursor()

c.execute("""
             CREATE TABLE IF NOT EXISTS  userdatabase(
            id INTEGER PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
            )
             """)

username1, password1 = "ramesh21", hashlib.sha256("ramesh21".encode()).hexdigest()
username2, password2 = "gukesh77", hashlib.sha256("chesschuss69".encode()).hexdigest()
username3, password3 = "mukesh331", hashlib.sha256("footballisgreat123".encode()).hexdigest()
username4, password4 = "ninja41", hashlib.sha256("passwordninja".encode()).hexdigest()

c.execute("INSERT INTO userdatabase (username, password) VALUES (?, ?)", (username1, password1))
c.execute("INSERT INTO userdatabase (username, password) VALUES (?, ?)", (username2, password2))
c.execute("INSERT INTO userdatabase (username, password) VALUES (?, ?)", (username2, password2))
c.execute("INSERT INTO userdatabase (username, password) VALUES (?, ?)", (username3, password3))
c.execute("INSERT INTO userdatabase (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()