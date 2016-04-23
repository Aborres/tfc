"""
  utils.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  April 2016
"""
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

def CheckOldFolder(path):
  if (CheckFolder(path)):
    print("\nRemoving Old Folder..\n")
    EraseFiles(path)

def CreateFolder(path):
  os.mkdir(path)