"""
  command.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  April 2016
"""
import sys
import ConfigParser
import os
from ftplib import FTP
from utils import *


class Command:

  def __init__(self):
    self.name = ""
    self.commands = {}
    self.commands_function = {}
    self.user = ""
    self.server = ""
    self.password = ""
    self.port = 0
    self.copy_dir = ""
    self.dest = ""
    self.assets = ""
    self.ftp = FTP()
    self.folder = ".tfc"
    self.config_file = "config.ini"
    self.config_path = self.folder + os.path.sep + self.config_file
    self.config_file_content = """[Server]
server =
port =
user =
password =

[FTP Dir]
current_dir =
last_check_time =

[Local]
copy_dir =
dest =
server_folder ="""

  def addArg(self, command, arg):
    self.commands[command] = arg

  def checkCommand(self, command):
    if command in self.commands_function:
      return True
    return False

  def checkNoArg(self, file):
    if(file):
      self.argError(file)

  def error(self, command, arg):
    print(self.name + " command " + command + " " + arg + "not found" )

  def runCommand(self, command, arg):
    self.commands_function[command](arg)

  def execute(self):
    if(len(self.commands) != 0):
      for execute_command in self.commands:
        if (self.checkCommand(execute_command)):
          self.runCommand(execute_command, self.commands[execute_command])
    else:
      self.default()


  def checkCreateFolder(self):
    if (CheckFolder(self.folder) == False):
      CreateHiddenFolder(self.folder)
      fb = open(self.config_path, 'w')
      fb.write(self.config_file_content)
      fb.close()
    else:
      print("tfc already exists in this folder")

  def readConfig(self):
    if(CheckFolder(self.folder) == True):
      config = ConfigParser.ConfigParser()
      config.read(self.config_path)
      self.server = config.get('Server', 'server')
      self.port = config.get('Server', 'port')
      self.user = config.get('Server', 'user')
      self.password = config.get('Server', 'password')
      self.copy_dir = config.get('Local', 'copy_dir')
      self.dest = config.get('Local', 'dest')
      self.server_folder = config.get('Local', 'server_folder')
      return True
    else:
      print("tfc not initialized in this folder")
      return False

  def default(self):
    print("Default")

  def help(self):
    print("Help")

  def connect(self):
    if(self.readConfig()):
      try:
        self.ftp = FTP(self.server)
        self.ftp.login(self.user, self.password)
        return True
      except Exception, e:
        print("ftc Unable to log in...")
        return False

  def showWelcome(self):
    if(self.connect()):
      print("\n" + self.ftp.getwelcome() + "\n")
      self.disconnect()
    
  def showDir(self):
    if(self.connect()):
      self.ftp.dir()
      self.disconnect()

  def disconnect(self):
    self.ftp.quit()

  def argError(self, file):
    print("tfc unexpected argument: " + str(file))
    sys.exit(-1)