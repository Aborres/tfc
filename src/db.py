"""
  db.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  May 2016
"""
import sqlite3
from hash import *

def_path = 'ftp_files.db'

def CreateDB(path):
  db = sqlite3.connect(path)
  db_cursor = db.cursor()

  db_cursor.execute('''
    CREATE TABLE DATA(
      ID INTEGER PRIMARY KEY AUTOINCREMENT,
      NAME VARCHAR(20) NOT NULL,
      PATH VARCHAR(200) NOT NULL,
      FILE_ID VARCHAR(100) NOT NULL
    );''')

  db.commit()
  db.close()

def CheckFileDB(path, name, file_path):
  exists = False

  db = sqlite3.connect(path)
  db_cursor = db.cursor()

  t = (name, file_path)
  db_cursor.execute('''
    SELECT * FROM DATA WHERE NAME == ? AND
    PATH == ?
    ''', t)
  if(db_cursor.fetchall()):
    exists = True

  db.commit()
  db.close()  

  return exists

def InsertFileDB(path, name, file_path, file_id):
  db = sqlite3.connect(path)
  db_cursor = db.cursor()  
  db_cursor.execute('''
    INSERT INTO DATA(NAME, PATH, FILE_ID) VALUES(?,?,?)''', [name, file_path, file_id])  
  db.commit()
  db.close()

def ShowContentDB(path):

  db = sqlite3.connect(path)
  db_cursor = db.cursor()

  db_cursor.execute('''SELECT * FROM DATA''')

  db_info = db_cursor.fetchall()

  for row in db_info:
    print row

  db.commit()
  db.close()  

def DeleteFileDB(path, name, file_path):
  db = sqlite3.connect(path)
  db_cursor = db.cursor()  
  db_cursor.execute('''
    DELETE FROM DATA WHERE 
    NAME == ? AND PATH == ?''', [name, file_path])
  db.commit()
  db.close()

def ModifyFileDB(path, name, file_path, file_id):
  db = sqlite3.connect(path)
  db_cursor = db.cursor()  
  db_cursor.execute('''
    UPDATE DATA
    SET FILE_ID = ?
    WHERE NAME == ? AND PATH == ?''', [file_id, name, file_path])
  db.commit()
  db.close()

def PurgeDB(path):
  db = sqlite3.connect(path)
  db_cursor = db.cursor()  
  db_cursor.execute('''DELETE FROM DATA''')
  db.commit()
  db.close()

def GetCRC32DB(path, name, file_path):
  file_id = ""
  db = sqlite3.connect(path)
  db_cursor = db.cursor()  
  db_cursor.execute('''
    SELECT FILE_ID FROM DATA WHERE NAME == ? AND
    PATH == ?
    ''', [name, file_path])
  file_id = db_cursor.fetchone()
  db.commit()
  db.close()
  return file_id[0] #list from select