"""
  dir.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  April 2016
"""
from utils import *
from command import Command

class Dir(Command):

  def __init__(self):
    Command.__init__(self)
    self.commands_function["-mkdir"] = self.makeDirectory
    self.commands_function["-makedir"] = self.makeDirectory
    self.commands_function["-ls"] = self.listDirectory
    self.commands_function["-list"] = self.listDirectory
    self.commands_function["-e"] = self.erase
    self.commands_function["-erase"] = self.erase
    self.commands_function["-ef"] = self.eraseFolder
    self.commands_function["-erasefolder"] = self.eraseFolder
    self.commands_function["-p"] = self.purge
    self.commands_function["-purge"] = self.purge

  def default(self):
    self.showDir()

  def makeDirectory(self, arg):
    if(self.connect()):
      for command in arg:
        try:
          self.ftp.mkd(command)
        except Exception, e:
          print("tfc " + command + " not found")
      self.disconnect()

  def listDirectory(self, arg):
    if(self.connect()):
      if(len(arg)!= 0):
        for command in arg:
          try:
            self.ftp.dir(command)
          except Exception, e:
            print("tfc " + command + " not found")
      else:
        self.ftp.dir("")
      self.disconnect()

  def erase(self, arg):
    if(self.connect()):
      for command in arg:
        try:
          self.ftp.delete(command)
        except Exception, e:
          print("tfc " + command + " not found")
      self.disconnect()

  def eraseFolder(self, arg):
    if(self.connect()):
      for command in arg:
        FTPRemoveTree(self.ftp, command)
      self.disconnect()

  #TODO
  def purge(self, arg):
    if(self.connect()):
      try:
        FTPRemoveTree(self.ftp, "")
      except Exception, e:
        print("tfc can not purgue server")
      self.disconnect()    