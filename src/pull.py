"""
  pull.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  April 2016
"""
import os
from command import Command
from utils import *
from db import *
from hash import *

class Pull(Command):

  def __init__(self):
    Command.__init__(self)
    self.commands_function["-f"] = self.pullFile
    self.commands_function["-file"] = self.pullFile

  def pullFile(self, files):
    if(self.connect()):
      for file in files:
        self.__downloadData(self.ftp, file, "")
      self.disconnect()

  def default(self):
    if(self.connect()):
      ftp = self.ftp
      ftp_files = ftp.nlst()
      new_path = "tfc_download"

      if(new_path[0] == "/"):
        new_path = new_path.replace("/", "")

      for ftp_file in ftp_files:
        if (ftp_file != '.' and ftp_file != '..' and ftp_file != '.ftpquota'):
          print("tfc donwloading: " + ftp_file + "\n")

          try:
            ftp.cwd(ftp_file) #if folder
            ftp.cwd("..")
            new_path += "/" + ftp_file

            if(CheckFolder(new_path) == False):
              CreateFullPath(new_path)

            self.__downloadFolder(ftp, ftp_file, new_path)
            ftp.cwd("..")
            new_path = new_path.rsplit("/", 1)[0]
          except Exception, e:
            self.__downloadFile(ftp, ftp_file, new_path + "/" + ftp_file)
      self.disconnect()

  def help(self, args):
    for arg in args:
      self.printHelp("pull", arg)

  def __downloadData(self, ftp, server_path, path):
    ext = server_path.rsplit(".", 1)
    file_name = server_path.rsplit("/", 1)
    file_name = file_name[len(file_name) - 1]
    file_path = server_path

    if (CheckFolder(file_path) == False):
      CreateFullPath(file_path)

    if (len(ext) > 1): #FILE
      try:
        self.__downloadFile(ftp, server_path, file_path)
      except Exception, e:
        erase = server_path.split("/", 1)[0]
        #EraseFiles(erase) TODO
        print("tfc file: " + server_path + " not found on server")
    else: #Folder
      try:
        self.__downloadFolder(ftp, server_path, file_path)
      except Exception, e:
        EraseFiles(path)
        print("tfc Folder: " + server_path + " not found on server")

  def __downloadFolder(self, ftp, path, local_path):
    ftp.cwd(path)
    ftp_files = ftp.nlst()
    new_path = local_path

    if(new_path[0] == "/"):
      new_path = new_path.replace("/", "")

    for ftp_file in ftp_files:
      if (ftp_file != '.' and ftp_file != '..' and ftp_file != '.ftpquota'):
        print("tfc donwloading: " + ftp_file + "\n")

        try:
          ftp.cwd(ftp_file) #if folder
          ftp.cwd("..")
          new_path += "/" + ftp_file

          if(CheckFolder(new_path) == False):
            CreateFullPath(new_path)

          self.__downloadFolder(ftp, ftp_file, new_path)
          ftp.cwd("..")
          new_path = new_path.rsplit("/", 1)[0]
        except Exception, e:
          self.__downloadFile(ftp, ftp_file, new_path + "/" + ftp_file)

  # Donwloads an especific file and replies the folder structure
  # Updates DB
  def __downloadFile(self, ftp, path, local_path):
    file_name = local_path.rsplit("/", 1)
    file_name = file_name[len(file_name) - 1]
    file_path = local_path

    st = 'RETR %s' % path
    ftp.retrbinary(st, open(local_path, 'wb').write)
    file_id = GetCRC32(local_path)

    if (CheckFileDB(self.db_path, file_name, file_path) == False):
      InsertFileDB(self.db_path, file_name, file_path, file_id)

    elif (GetCRC32DB(self.db_path, file_name, file_path) !=
     file_id):
      ModifyFileDB(self.db_path, file_name, file_path, file_id)

  def __checkFolder(self):
    if (CheckFolder(self.dest) == False):
      CreateFolder(self.dest)

  def __moveFolder(self):
    if (checkFolder(self.copy_dir) == False):
      CreateFolder(self.copy_dir)
    CopyFiles(self.dest, self.copy_dir)
    EraseFiles(self.dest)
