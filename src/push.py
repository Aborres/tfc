"""
  push.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  April 2016
"""
import os
from command import Command

class Push(Command):

  def __init__(self):
    Command.__init__(self)
    self.commands_function["-f"] = self.uploadFile
    self.commands_function["-e"] = self.eraseDefault
    self.commands_function["-ef"] = self.eraseUploadFile

  def uploadFile(self, file):
    self.connect()
    if (os.path.isfile(file) != True):
      try:
        self.ftp.mkd(file)
      except Exception, e:
        print("tfc Updating folder")
      self.ftp.cwd(file)
    self.__uploadData(self.ftp, file, False)
    self.disconnect()

  def eraseDefault(self, file):
    self.connect()
    self.__uploadData(self.ftp, self.copy_dir, True)
    self.disconnect()

  def eraseUploadFile(self, file):
    self.connect()
    self.__uploadData(self.ftp, file, True)
    self.disconnect()

  def default(self):
    self.connect()
    self.__uploadData(self.ftp, self.copy_dir, False)
    self.disconnect()

  def __uploadData(self, ftp, path, erase):
    try:
      files = os.listdir(path)

      print("Files to upload from " + path + ": ")
      print(files)

      for f in files:

        ftp_path = path + os.path.sep +  f

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
      print("tfc " + file + " uploaded")
    except Exception, e:
      print("File: " + file + " not found")