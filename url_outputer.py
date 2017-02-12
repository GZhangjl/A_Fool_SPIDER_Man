import sqlite3

class UrlOutputer():
    def __init__(self):
        self.data=[]

    def collector(self,url_data):
        if url_data != None:
            self.data.append(url_data)
        else:
            return None
            
    def output_data(self):
        connection=sqlite3.connect("The_Witcher_baike.sqlite")
        cursor=connection.cursor()
        cursor.execute("""CREATE TABLE summary(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            url TEXT NOT NULL,
            title TEXT NOT NULL,
            summary TEXT NOT NULL)""")
        connection.commit()
        for data in self.data:
            cursor.execute("INSERT INTO summary (url,title,summary) VALUES (?,?,?)",(data["url"],data["title"],data["summary"]))
            connection.commit()
        connection.close()