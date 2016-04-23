"""
  upload.py Python Script

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

  UploadData(ftp, dest)
  
  ftp.quit()
  
  print("\nDisconected from server...\n")

def UploadData(ftp, path):
  files = os.listdir(path)

  print("Files to upload from " + path + ": ")
  print(files)

  for f in files:

    ftp_path = path + os.path.sep +  f

    if (os.path.isfile(ftp_path)):
      print("\nUploading: " + ftp_path + "\n")
      fb = open(ftp_path, 'rb')
      ftp.storbinary('STOR %s' % f, fb)
      fb.close()
    elif (os.path.isdir(ftp_path)):
      print("ERASING: " + f)
      FtpRmTree(ftp, f)
      try:
        ftp.mkd(f)
      except Exception, e:
        print("Folder was there")  
      ftp.cwd(f)
      UploadData(ftp, ftp_path)
      ftp.cwd("../")

def FtpRmTree(ftp, path):
  """Recursively delete a directory tree on a remote server."""
  wd = ftp.pwd()

  try:
    names = ftp.nlst(path)
  except Exception, e:
    # some FTP servers complain when you try and list non-existent paths
    print('FtpRmTree: Could not remove {0}: {1}'.format(path, e))
    return

  for name in names:
    if os.path.split(name)[1] in ('.', '..'): continue

    print('FtpRmTree: Checking {0}'.format(name))

    try:
      ftp.cwd(name)  # if we can cwd to it, it's a folder
      ftp.cwd(wd)  # don't try a nuke a folder we're in
      FtpRmTree(ftp, name)
    except Exception, e:
      ftp.delete(path + '/' + name)

  try:
    ftp.rmd(path)
  except Exception, e:
    print('FtpRmTree: Could not remove {0}: {1}'.format(path, e))

if __name__ == "__main__":
  print("\n************ Upload Script ************")

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
  CopyFiles(copy_dir, dest)
  FTPConexion()
  EraseFiles(dest)
  print("\n***************************************")