"""
  command.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  April 2016
"""
import sys
import ConfigParser
import os
import getpass
import json
from ftplib import FTP_TLS
from utils import *
from print_color import *

class Command:

  def __init__(self):
    self.name = ""
    self.commands = {}
    self.commands_function = {}
    self.user = ""
    self.server = ""
    self.port = 0
    self.copy_dir = ""
    self.dest = ""
    self.assets = ""
    self.ftp = FTP_TLS()
    self.folder = ".tfc"
    self.config_file = "config.ini"
    self.config_path = self.folder + os.path.sep + self.config_file
    self.config_file_content = ""
    self.db_name = "ftp_files.db"
    self.db_path = self.folder + os.path.sep + self.db_name
    self.place_holder_config = "files/config.ini"
    self.help_path = "files/help.json"

  def addArg(self, command, arg):
    l = list()
    for a in arg:
        l.append(a.replace("\\", "/"))
    self.commands[command] = l

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
      
      with open(self.place_holder_config, 'r') as content_file:
        self.config_file_content += content_file.read()

      fb = open(self.config_path, 'w')
      fb.write(self.config_file_content)
      fb.close()

    else:
      print(color.TFC + "tfc " + color.WARNING + "already exists in this folder")

  def readConfig(self):
    if(CheckFolder(self.folder) == True):
      config = ConfigParser.ConfigParser()
      config.read(self.config_path)
      self.server = config.get('Server', 'server')
      self.port = config.get('Server', 'port')
      self.user = config.get('Server', 'user')
      self.copy_dir = config.get('Local', 'copy_dir')
      self.dest = config.get('Local', 'dest')
      self.server_folder = config.get('Local', 'server_folder')
      return True
    else:
      print(color.TFC + "tfc " + color.WARNING + "not initialized in this folder")
      return False

  def default(self):
    print("Default")

  def help(self):
    print("Help")

  #TODO: Check security conection
  def connect(self):
    if(self.readConfig()):
      try:
        self.ftp = FTP_TLS(self.server)
        password = self.__askPassWord()
        self.ftp.login(self.user, password)
        #self.ftp.prot_p()
        return True
      except Exception, e:
        print(color.TFC + "ftc " + color.WARNING + "Unable to log in...")
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

  def printHelp(self, command, arg):
    with open(self.help_path) as help_file:
          help = json.load(help_file)
    if (len(arg) == 0):
      print("tfc " + help["help"][command][""])
    else:
      for i in len(arg):
        try:
          print("tfc " + help["help"][command][arg])
        except Exception, e:
          print(color.TFC + "tfc " + color.WARNING + "help command " + color.COMMAND + arg +
          color.WARNING + " not found")

  def __askPassWord(self):
      return getpass.getpass(prompt="tfc password: ")

  def __askTimedPassWord(self):
      print "TIMED PASS"
