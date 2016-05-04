"""
  pull.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  April 2016
"""
import os
from command import Command
from utils import *

class Pull(Command):

  def __init__(self):
    Command.__init__(self)
    self.commands_function["-f"] = self.pullFile
    self.commands_function["-file"] = self.pullFile

  def pullFile(self, file):
    print("Full")

  def default(self):
    if(self.connect()):
      self.__checkFolder()
      self.__downloadData(self.ftp, "", self.dest)
      self.disconnect()

  def __downloadData(self, ftp, server_path, path):
    print("\nDonwloading from: " + server_path)
    
    ftp_files = ftp.nlst()
    print("Files to download:")
    print(ftp_files)

    for ftp_file in ftp_files:
      if (ftp_file != '.' and ftp_file != '..' and ftp_file != '.ftpquota'):
        print("Donwloading: ")
        print(ftp_file + "\n")

        local_path = path + os.path.sep + ftp_file   
        server_file = server_path + "/" + ftp_file

        try:
          ftp.cwd(server_file)

          if (CheckFolder(local_path) == False):
            CreateFolder(local_path)
          
          self.__downloadData(ftp, server_file, local_path)

        except Exception, e:
          st = 'RETR %s' % server_file
          
          ftp.retrbinary(st, open(local_path, 'wb').write)


  def __checkFolder(self):
    if (CheckFolder(self.dest) == False):
      CreateFolder(self.dest)

  def __moveFolder(self):
    if (checkFolder(self.copy_dir) == False):
      CreateFolder(self.copy_dir)
    CopyFiles(self.dest, self.copy_dir)
    EraseFiles(self.dest)