import subprocess

class RunCommand:
    def __init__(self=None,command=None,status=None,error=None,output=None):
        self.command = command
        self.status = status
        self.stderror = error
        self.stdout = output

    def Run_Command(self,command):
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
        else:
            print(f"Image built successfully: {result.stdout}")


# run = RunCommand("ls")
# print(run.Run_Command())
# print(run.status)



