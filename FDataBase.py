import sqlite3 as sq
class FDataBase:
    def __init__(self, db) -> None:
        self.__db = db
        self.__cur = self.__db.cursor()
    
    def getNotes(self):
        sql = 'SELECT * FROM notes'
        self.__cur.execute(sql)
        res = self.__cur.fetchall()

        return res

    def addNote(self, text):
        sql = 'INSERT INTO notes VALUES(NULL, ?)'
        self.__cur.execute(sql, (text, ))
        self.__db.commit()
        
        return True

    def deleteNote(self, id):
        sql = 'DELETE FROM notes WHERE id = ?'
        self.__cur.execute(sql, (id, ))
        self.__db.commit()