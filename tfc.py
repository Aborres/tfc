"""
  main.py Python Script

  Jose Manuel Naranjo Temprano <jmnaranjotemprano@gmail.com>
  April 2016
"""
import os
import sys
sys.path.insert(0, 'src/')
from main import TFC
from utils import *
from db import *
from hash import *

if __name__ == "__main__":
  tfc = TFC()
  tfc.run()
