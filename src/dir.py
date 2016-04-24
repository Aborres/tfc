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
    self.commands_function["-ls"] = self.listDirectory
    self.commands_function["-e"] = self.erase
    self.commands_function["-ef"] = self.eraseFolder

  def default(self):
    self.showDir()

  def makeDirectory(self, arg):
    if(self.connect()):
      try:
        self.ftp.mkd(arg)
      except Exception, e:
        print("tfc " + arg + " not found")
      self.disconnect()

  def listDirectory(self, arg):
    if(self.connect()):
      try:
        self.ftp.dir(arg)
      except Exception, e:
        print("tfc " + arg + " not found")
      self.disconnect()

  def erase(self, arg):
    if(self.connect()):
      try:
        self.ftp.delete(arg)
      except Exception, e:
        print("tfc " + arg + " not found")
      self.disconnect()

  def eraseFolder(self, arg):
    if(self.connect()):
      FTPRemoveTree(self.ftp, arg)
      self.disconnect()