"""
  push.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  April 2016
"""
import os
from command import Command
from db import *

class Push(Command):

  def __init__(self):
    Command.__init__(self)
    self.commands_function["-f"] = self.uploadFile
    self.commands_function["-file"] = self.uploadFile
    self.commands_function["-e"] = self.eraseDefault
    self.commands_function["-erase"] = self.eraseDefault
    self.commands_function["-ef"] = self.eraseUploadFile
    self.commands_function["-erasefile"] = self.eraseUploadFile
    self.commands_function["-h"] = self.help
    self.commands_function["-help"] = self.help

  def uploadFile(self, files):
    if(self.connect()):
      for file in files:
        if (os.path.isfile(file) != True):
          try:
            self.ftp.mkd(file)
          except Exception, e:
            print("tfc Updating folder")
            print(file)
          self.ftp.cwd(file)
          self.__uploadData(self.ftp, file, False)
        else:
          path = file.rsplit("/", 1)[0]
          try:
            print path
            CreateFullPathFTP(self.ftp, path)
            #self.ftp.mkd(path)
          except Exception, e:
            pass
          self.__pushFile(self.ftp, file, file)
      self.disconnect()

  def eraseDefault(self, file):
    self.checkNoArg(file)

    if(self.connect()):
      self.__uploadData(self.ftp, self.copy_dir, True)
      self.disconnect()

  def eraseUploadFile(self, file):
    if(self.connect()):
      for file in files:
        if (os.path.isfile(file) != True):
          try:
            self.ftp.mkd(file)
          except Exception, e:
            print("tfc Updating folder")
          self.ftp.cwd(file)
        self.__uploadData(self.ftp, file, True)
      self.disconnect()

  def default(self):
    if(self.connect()):
      self.__uploadData(self.ftp, os.getcwd(), False)
      self.disconnect()

  def help(self, args):
    self.printHelp("push", arg)

  def __uploadData(self, ftp, path, erase):
    try:
      files = os.listdir(path)

      print("Files to upload from " + path + ": ")
      print(files)

      for f in files:

        ftp_path = path + "/" +  f

        if (os.path.isfile(ftp_path)):
          print("\nUploading: " + ftp_path + "\n")
          self.__pushFile(ftp, f, ftp_path)
        elif (os.path.isdir(ftp_path)):
          if (erase):
            print("ERASING: " + f)
            self.FTPRemoveTree(ftp, f)
          try:
            ftp.mkd(f)
          except Exception, e:
            print("Folder was there")
          ftp.cwd(f)
          self.__uploadData(ftp, ftp_path, erase)
          ftp.cwd("../")
    except Exception, e:
      self.__pushFile(ftp, path, path)

  def __pushFile(self, ftp, f, file):
    try:
      fb = open(file, 'rb')
      ftp.storbinary('STOR %s' % f, fb)
      fb.close()
      
      file_name = file.rsplit("/", 1)
      file_name = file_name[len(file_name) - 1]
      file_path = file
      file_id = GetCRC32(file)

      if (CheckFileDB(self.db_path, file_name, file_path) == False):
        InsertFileDB(self.db_path, file_name, file_path, file_id)
      else:
        if(GetCRC32DB(self.db_path, file_name, file_path) != file_id):
          ModifyFileDB(self.db_path, file_name, file_path, file_id)
      print("tfc " + file + " uploaded")

    except Exception, e:
      print("File: " + file + " not found")
