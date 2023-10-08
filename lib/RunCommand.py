import subprocess
import os
class RunCommand:
    def __init__(self=None,command=None,status=None,error=None,output=None):
        self.command = command
        self.status = status
        self.stderror = error
        self.stdout = output

    def Run_Command(self,command):
        print(command)
        os.system('docker run -d --name b9fa87a5a0fa56dd9e48 flask:1.0')
        print("Done")
        os.system('docker start 8fb378a47a65cc822f07')
        print("Running")
        # command = "ls"
        # result = subprocess.call(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # if result.returncode != 0:
        #     print(f"Error: {result.stderr}")
        # else:
        #     print(f"Image built successfully: {result.stdout}")


# run = RunCommand("ls")
# print(run.Run_Command())
# print(run.status)



