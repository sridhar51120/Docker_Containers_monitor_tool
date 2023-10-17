import os
import subprocess
import sys
class Windows:
    def __init__(self,strart_dir = None,path=None):
        self.strart_dir = "C:\\"
        self.path = self.dockerExeFile
        
    def dockerExeFile(self):
        for root, _, files in os.walk(self.strart_dir):
            if "docker.exe" in files:
                return os.path.join(root, "docker.exe")
        return None
    
    
    def addExecutable(self,directory):
        if directory and os.path.exists(directory):
            path = os.environ.get("PATH", "")
            if directory not in path:
                os.environ["PATH"] = f"{directory};{path}"
                # print(os.environ["PATH"])
                return True

 
    