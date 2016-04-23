"""
  download.py Python Script
  
  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  April 2016
"""
from utils import *
from ftplib import FTP

def FTPConexion():

  ftp = FTP(server)
  
  ftp.login(user, password)
  
  print("\n" + ftp.getwelcome() + "\n")
  ftp.dir()

  DownloadData(ftp, "", dest)

  ftp.quit()

  print("\nDisconected from server...\n")

def DownloadData(ftp, server_path, path):
  print("\nDonwloading from: " + server_path)
  
  ftp_files = ftp.nlst()
  print("Files to download:")
  print(ftp_files)

  for ftp_file in ftp_files:
    if (ftp_file != '.' and ftp_file != '..' and ftp_file != '.ftpquota'):
      print("Donwloading: ")
      print(ftp_file + "\n")

      local_path = path + os.path.sep + ftp_file   
      server_file = server_path + "/" + ftp_file

      try:
        ftp.cwd(server_file)

        if (CheckFolder(local_path) == False):
          CreateFolder(local_path)
        
        self.__downloadData(ftp, server_file, local_path)

      except Exception, e:
        st = 'RETR %s' % server_file
        
        ftp.retrbinary(st, open(local_path, 'wb').write)

if __name__ == "__main__":
  print("\n************ Download Script ************")

  info = ReadConfig('config.ini')
  
  #FTP info
  server = info['server']
  port = info['port']
  user = info['user']
  password = info['password']
  copy_dir = info['copy_dir']
  dest = info['dest']
  server_folder = info['server_folder']

  CheckOldFolder(dest)
  CreateFolder(dest)
  FTPConexion()
  CheckOldFolder(copy_dir)
  CopyFiles(dest, copy_dir)
  EraseFiles(dest)
  print("\n*****************************************")