"""
  pull.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  May 2016
"""
from db import *
from command import Command

class Purgue(Command):

  def __init__(self):
    Command.__init__(self)
    self.commands_function["-db"] = self.dataBase
    self.commands_function["-database"] = self.dataBase
    self.commands_function["-s"] = self.server
    self.commands_function["-server"] = self.server
    self.commands_function["-l"] = self.local
    self.commands_function["-local"] = self.local

  def dataBase(self, args):
    PurgeDB(self.db_path)

  def server(self, args):
    if(self.connect()):
      try:
        FTPRemoveTree(self.ftp, "")
      except Exception, e:
        print(color.TFC + "tfc " + color.FAIL + "can not purgue server")
      self.disconnect()

  def local(self, args):
    print "LOCAL"
