import os
from lib.Windows import Windows

win = Windows()
if(win.dockerExeFile()):
    path = win.dockerExeFile()
    if win.addExecutable(path):
      print(f"Added Docker path: {os.path.dirname(path)} to PATH.")
