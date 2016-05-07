"""
  utils.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  April 2016
"""
import tempfile
import shutil
import errno
import os
import ConfigParser

def CopyFiles(from_folder, to_folder):
  print("\nCoping files...\n")
  
  try:
    shutil.copytree(from_folder, to_folder)
  except OSError as exc:
    if exc.errno == errno.ENOTDIR:
      shutil.copy(from_folder, to_folder)
    else: raise

def EraseFiles(file):
  print("\nErasing files...\n")
  if (CheckFolder(file)):
    shutil.rmtree(file)

def CheckFolder(path):
  exists = False
  if (os.path.exists(path)):
    exists = True
  return exists

def CreateFile(path):
  if(CheckFolder(path) == False):
    f = open(path, "wb")
    f.close()
  else:
    print("File " + path + " was already there")

def CheckOldFolder(path):
  if (CheckFolder(path)):
    print("\nRemoving Old Folder..\n")
    EraseFiles(path)

def CreateFolder(path):
  os.mkdir(path)

def CreateHiddenFolder(folder_name):
  path = os.getcwd()
  p = tempfile.mkdtemp(dir=path)
  f = p.split(path + "/")[1]
  os.rename(f, folder_name)

def FTPRemoveTree(ftp, path):
  folders = ftp.pwd()
  print(folders)
  try:
    files = ftp.nlst(path)
  except Exception, e:
    print('Failed to remove {0}: {1}'.format(path, e))
    return

  for f in files:
    if os.path.split(f)[1] in ('.', '..'): continue

    try:
      ftp.cwd(f)
      ftp.cwd(folders)
      self.__ftpRemoveTree(ftp, f)
    except Exception, e:
      ftp.delete(path + '/' + f)

  try:
    ftp.rmd(path)
  except Exception, e:
    print('Failed to remove {0}: {1}'.format(path, e))

def __pushFile(self, ftp, f, file):
  try:
    fb = open(file, 'rb')
    ftp.storbinary('STOR %s' % f, fb)
    fb.close()
    print("tfc " + file + " uploaded")
  except Exception, e:
    print("File: " + file + " not found")