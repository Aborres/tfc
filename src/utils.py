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
import time

def CopyFiles(from_folder, to_folder):
  print("\nCoping files...\n")

  try:
    shutil.copytree(from_folder, to_folder)
  except OSError as exc:
    if exc.errno == errno.ENOTDIR:
      shutil.copy(from_folder, to_folder)
    else: raise

def ConvertSep(text):
  aux = text.replace("\\", os.path.sep)
  aux.replace("/", os.path.sep)
  return aux

def EraseFiles(file):
  text = ConvertSep(file)
  if (CheckFolder(text)):
    shutil.rmtree(text)

def CheckFolder(path):
  text = ConvertSep(path)
  exists = False
  if (os.path.exists(text)):
    exists = True
  return exists

def CreateFile(path):
  text = ConvertSep(path)
  if(CheckFolder(text) == False):
    f = open(text, "wb")
    f.close()
  else:
    print("File " + text + " was already there")

def CheckOldFolder(path):
  text = ConvertSep(path)
  if (CheckFolder(text)):
    print("\nRemoving Old Folder..\n")
    EraseFiles(text)

def CreateFolder(path):
  text = ConvertSep(path)
  os.mkdir(text)

def CreateFullPath(path):
  text = ConvertSep(path)
  new_path = text.split("/")
  accum_path = new_path[0]

  it = 1
  for i in range(0, len(new_path)):
    if (CheckFolder(accum_path) == False):
      CreateFolder(accum_path)
    else:
      accum_path += "/" + new_path[it]
      it += 1

def CreateFullPathFTP(ftp, path):
  text = ConvertSep(path)
  new_path = text.split("/")
  for i in range(len(new_path)):
    try:
      ftp.mkd(new_path[i])
    except Exception, e:
      pass
    ftp.cwd(new_path[i])
  for i in range(len(new_path)):
    ftp.cwd("..")

def CreateHiddenFolder(folder_name):
  path = os.getcwd()
  p = tempfile.mkdtemp(dir=path)
  f = p.split(path + os.path.sep)[1]
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

def GetTime():
  t = time.localtime()
  return t.tm_hour * 3600 + t.tm_min * 60 + t.tm_sec

def __pushFile(self, ftp, f, file):
  try:
    fb = open(file, 'rb')
    ftp.storbinary('STOR %s' % f, fb)
    fb.close()
    print("tfc " + file + " uploaded")
  except Exception, e:
    print("File: " + file + " not found")
