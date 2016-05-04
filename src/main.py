"""
  tfc.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  April 2016
"""
import sys
from init import Init
from push import Push
from pull import Pull
from dir import Dir
from config import Config
from collections import defaultdict

class TFC():

  def __init__(self):
    self.closed = False
    self.command = str()
    self.args = defaultdict(list)
    self.command_history = list()
    self.valid_commands = {}
    self.valid_commands["init"] = Init()
    self.valid_commands["push"] = Push()
    self.valid_commands["config"] = Config()
    self.valid_commands["pull"] = Pull()
    self.valid_commands["dir"] = Dir()

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
    argc = sys.argv
    try:
      self.command = argc[1]
      command = ""
      input_arg = ""
      it = 0
      for arg in argc:
        try:
          if (arg[0] == "-"):
            command = arg
            try:
              counter = 1
              argv = argc[it + counter]
              while argv[0] != "-" and (it + counter) < len(argc):
                input_arg = argc[it + counter]
                self.args[command].append(input_arg)
                counter += 1
                if ((it + counter) < len(argc)):
                  argv = argc[it + counter] 
            except Exception, e:
              print("LLEGA")
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
