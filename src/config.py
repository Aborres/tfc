"""
  config.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  April 2016
"""
from command import Command

class Config(Command):

  def __init__(self):
    Command.__init__(self)
    self.commands_function["-u"] = self.setUser
    self.commands_function["-s"] = self.setServer
    self.commands_function["-p"] = self.setPort
    self.commands_function["-ps"] = self.setPassword
    self.commands_function["-uf"] = self.setUploadFolder
    self.commands_function["-df"] = self.setDownloadFolder
    self.commands_function["-h"] = self.help
    self.commands_function["-w"] = self.welcome
    self.commands_function["-i"] = self.info

  def writeConfig(self, section, tag, data):
    ini = ConfigParser.ConfigParser()
    ini.read(self.path)
    ini.set(section, tag, data)
    with open(self.path, 'wb') as configfile:
      ini.write(configfile)

  def setUser(self, user):
    self.checkCreateFolder()
    self.writeConfig('Server', 'user', user)

  def setServer(self, server):
    self.checkCreateFolder()
    self.writeConfig('Server', 'server', server)

  def setPort(self, port):
    self.checkCreateFolder()
    self.writeConfig('Server', 'port', port)

  def setPassword(self, password):
    self.checkCreateFolder()
    self.writeConfig('Server', 'password', password)

  def setUploadFolder(self, folder):
    self.checkCreateFolder()
    self.writeConfig('Local', 'copy_dir', folder)

  def setDownloadFolder(self, folder):
    self.checkCreateFolder()
    self.writeConfig('Local', 'dest', folder)

  def default(self):
    readConfig()
    print("Server: " + self.server)
    print("Port: " + self.port)
    print("User: " + self.user)
    print("Password: " + self.password)
    print("Local Dir: " + self.copy_dir)
    print("Local Dest: " + self.dest)
    print("Server Folder: " + self.assets)

  def help(self, arg):
    if (arg == ""):
      print("\ntfc config -> Manages basic ftp information")
      print("PARAMS:")
      print("tfc config -u + arg -> Sets arg as ftp user")
      print("tfc config -s + arg -> Sets arg as ftp ip")
      print("tfc config -p + arg -> Sets arg as ftp port")
      print("tfc config -ps + arg -> Sets arg as ftp password")
      print("tfc config -uf + arg -> Sets arg as ftp upload default folder")
      print("tfc config -df + arg -> Sets arg as ftp download default folder")
      print("tfc config -h + arg -> Shows help")
    elif (arg == "-u"):
      print("\ntfc config -u + arg -> Sets arg as ftp user")

  def welcome(self, arg):
    print("Welcome to TFC v.0 :)")

  def info(self, arg):
    print("TFC is developed by Jose Manuel Naranjo <jmnaranjotemprano@gmail> ")
