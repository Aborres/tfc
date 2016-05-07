"""
  init.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  May 2016
"""
from command import Command
from utils import * 
from db import *

class Init(Command):

  def __init__(self):
    Command.__init__(self)
    self.commands_function["-f"] = self.initForce
    self.commands_function["-force"] = self.initForce
    self.commands_function["-e"] = self.erase
    self.commands_function["-erase"] = self.erase
    self.commands_function["-c"] = self.clone
    self.commands_function["-clone"] = self.clone

  def default(self):
    self.checkCreateFolder()
    CreateDB(self.db_path)

  def initForce(self, arg):
    self.erase(None)
    self.default()

  def erase(self, arg):
    if(CheckFolder(self.folder) == True):
      EraseFiles(self.folder)

  def clone(self, arg):
    if (len(arg) == 2):
      from_path = arg[0]
      to_path = arg[1]
      CopyFiles(from_path, to_path)
    else:
      print("tfc Invalid args for clone")
