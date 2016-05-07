"""
  hash.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  May 2016
"""
import zlib
from utils import *

def GetCRC32(path):
  if (CheckFolder(path)):
    file_hash = 0
    for line in open(path, "rb"):
      file_hash = zlib.crc32(line, file_hash)
    return "%X"%(file_hash & 0xFFFFFFFF)