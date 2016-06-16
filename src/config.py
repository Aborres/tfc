"""
  config.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  April 2016
"""
from command import Command
from utils import *
from print_color import *

class Config(Command):

  def __init__(self):
    Command.__init__(self)
    self.commands_function["-u"] = self.setUser
    self.commands_function["-user"] = self.setUser
    self.commands_function["-s"] = self.setServer
    self.commands_function["-server"] = self.setServer
    self.commands_function["-p"] = self.setPort
    self.commands_function["-port"] = self.setPort
    self.commands_function["-ps"] = self.setPassword
    self.commands_function["-password"] = self.setPassword
    self.commands_function["-uf"] = self.setUploadFolder
    self.commands_function["-uploadfolder"] = self.setUploadFolder
    self.commands_function["-df"] = self.setDownloadFolder
    self.commands_function["-downloadfolder"] = self.setDownloadFolder
    self.commands_function["-timeout"] = self.setTimeOut
    self.commands_function["-h"] = self.help
    self.commands_function["-help"] = self.help
    self.commands_function["-w"] = self.welcome
    self.commands_function["-welcome"] = self.welcome
    self.commands_function["-i"] = self.info
    self.commands_function["-info"] = self.info

  def setUser(self, user):
    if (len(user) != 0):
      if (CheckFolder(self.folder) == True):
        self.__writeConfig('Server', 'user', user[0])
      else:
        print(color.TFC + "tfc " + color.WARNING + "was not initialized on this folder")
    else:
      print(color.TFC + "tfc " + color.WARNING + "not arguments recived")

  def setServer(self, server):
    if (len(server) != 0):
      if (CheckFolder(self.folder) == True):
        self.__writeConfig('Server', 'server', server[0])
      else:
        print(color.TFC + "tfc " + color.WARNING + "was not initialized on this folder")
    else:
      print(color.TFC + "tfc " + color.WARNING + "not arguments recived")

  def setPort(self, port):
    if (len(port) != 0):
      if (CheckFolder(self.folder) == True):
        self.__writeConfig('Server', 'port', port[0])
      else:
        print(color.TFC + "tfc " + color.WARNING + "was not initialized on this folder")
    else:
      print(color.TFC + "tfc " + color.WARNING + "not arguments recived")

  def setPassword(self, password):
    if (len(password) != 0):
      if (CheckFolder(self.folder) == True):
        self.__writeConfig('Server', 'password', password[0])
      else:
        print(color.TFC + "tfc " + color.WARNING + "was not initialized on this folder")
    else:
      print(color.TFC + "tfc " + color.WARNING + "not arguments recived")

  def setUploadFolder(self, folder):
    if (len(folder) != 0):
      if (CheckFolder(self.folder) == True):
        self.__writeConfig('Local', 'copy_dir', folder[0])
      else:
        print(color.TFC + "tfc " + color.WARNING + "was not initialized on this folder")
    else:
      print(color.TFC + "tfc " + color.WARNING + "not arguments recived")

  def setDownloadFolder(self, folder):
    if (len(folder) != 0):
      if (CheckFolder(self.folder) == True):
        self.__writeConfig('Local', 'dest', folder[0])
      else:
        print(color.TFC + "tfc " + color.WARNING + "was not initialized on this folder")
    else:
      print(color.TFC + "tfc " + color.WARNING + "not arguments recived")

  def setTimeOut(self, timeout):
    if (len(timeout) != 0):
      if (CheckFolder(self.folder) == True):
        self.__writeConfig('Config', 'time_out', timeout[0])
      else:
        print(color.TFC + "tfc " + color.WARNING + "was not initialized on this folder")
    else:
      print(color.TFC + "tfc " + color.WARNING + "not arguments recived")

  def default(self):
    if(self.readConfig()):
      print(color.TFC + "Server: " + color.ARG + self.server)
      print(color.TFC + "Port: " + color.ARG + str(self.port))
      print(color.TFC + "User: " + color.ARG + self.user)
      print(color.TFC + "Local Dir: " + color.ARG + self.copy_dir)
      print(color.TFC + "Local Dest: " + color.ARG + self.dest)
      print(color.TFC + "Server Folder: " + color.ARG + self.assets)

  def help(self, args):
    self.printHelp("config", args)

  def welcome(self, arg):
    print(color.TFC + "Welcome to TFC v.01 :)")

  def info(self, arg):
    print(color.TFC + "TFC is developed by Jose Manuel Naranjo")

  def __writeConfig(self, section, tag, data):
    ini = ConfigParser.ConfigParser()
    ini.read(self.config_path)
    ini.set(section, tag, data)
    with open(self.config_path, 'wb') as configfile:
      ini.write(configfile)
