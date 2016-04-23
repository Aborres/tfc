"""
  tfc.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  April 2016
"""
import sys
from push import Push
from pull import Pull
from config import Config

class TFC():

  def __init__(self):
    self.closed = False;
    self.command = str()
    self.args = {}
    self.command_history = list()
    self.valid_commands = {}
    self.valid_commands["push"] = Push()
    self.valid_commands["config"] = Config()
    self.valid_commands["pull"] = Pull()

  def checkCommand(self):
    for command in self.valid_commands:
      if(command == self.command):
        return True
    return False

  def executeCommand(self):
    if (self.checkCommand()):
      if (len(self.args) != 0):
        for command in self.args.keys():
          self.valid_commands[self.command].addArg(command, self.args[command])  
      self.valid_commands[self.command].execute()
    else:
      self.error()

  def history(self):
    for commands in self.command_history:
      print(commands)
    
  def readInput(self):
    try:
      self.command = sys.argv[1]
      command = ""
      input_arg = ""
      it = 0
      for arg in sys.argv:
        try:
          if (arg[0] == "-"):
            command = arg
            try:
              input_arg = sys.argv[it + 1]
              self.args[command] = input_arg
            except Exception, e:
              self.args[command] = ""
        except Exception, e:
            self.error()
        it += 1
    except Exception, e:
      print("tfc not arguments recived...")
      print("Try: tfc config -h to start")
      sys.exit(-1) #if nothing recieved abort program

  def run(self):
    self.readInput()
    self.executeCommand()

  def error(self):
    print("tfc command \"" + self.command + "\" not found")