"""
  config.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  April 2016
"""
from command import Command
from utils import *

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
    self.commands_function["-h"] = self.help
    self.commands_function["-help"] = self.help
    self.commands_function["-w"] = self.welcome
    self.commands_function["-welcome"] = self.welcome
    self.commands_function["-i"] = self.info
    self.commands_function["-info"] = self.info

  def setUser(self, user):
    if (CheckFolder(self.folder) == True):
      self.__writeConfig('Server', 'user', user[0])
    else:
      print("tfc was not initialized on this folder")

  def setServer(self, server):
    if (CheckFolder(self.folder) == True):
      self.__writeConfig('Server', 'server', server[0])
    else:
      print("tfc was not initialized on this folder")

  def setPort(self, port):
    print(port)
    if (CheckFolder(self.folder) == True):
      self.__writeConfig('Server', 'port', port[0])
    else:
      print("tfc was not initialized on this folder")

  def setPassword(self, password):
    print("PASSWORD: " + password[0])
    if (CheckFolder(self.folder) == True):
      self.__writeConfig('Server', 'password', password[0])
    else:
      print("tfc was not initialized on this folder")

  def setUploadFolder(self, folder):
    if (CheckFolder(self.folder) == True):
      self.__writeConfig('Local', 'copy_dir', folder[0])
    else:
      print("tfc was not initialized on this folder")

  def setDownloadFolder(self, folder):
    if (CheckFolder(self.folder) == True):
      self.__writeConfig('Local', 'dest', folder[0])
    else:
      print("tfc was not initialized on this folder")

  def default(self):
    if(self.readConfig()):
      print("Server: " + self.server)
      print("Port: " + str(self.port))
      print("User: " + self.user)
      print("Local Dir: " + self.copy_dir)
      print("Local Dest: " + self.dest)
      print("Server Folder: " + self.assets)

  def help(self, args):
    for arg in args:
      self.printHelp("config", arg)

  def welcome(self, arg):
    print("Welcome to TFC v.01 :)")

  def info(self, arg):
    print("TFC is developed by Jose Manuel Naranjo <jmnaranjotemprano@gmail> ")

  def __writeConfig(self, section, tag, data):
    ini = ConfigParser.ConfigParser()
    ini.read(self.config_path)
    ini.set(section, tag, data)
    with open(self.config_path, 'wb') as configfile:
      ini.write(configfile)
