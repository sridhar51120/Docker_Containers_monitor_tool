import subprocess
class RootUser:
    def __init__(self,command: list):
        self.Script_Command = command

    def isRootUser(self):
        # command = ["sudo", "python3", "test.py"] 
        try:
            result = subprocess.run(self.Script_Command, capture_output=True, text=True, check=True)
            print("Command output:")
            print(result.returncode)
        except subprocess.CalledProcessError as e:
            print("Error executing the command:")
            print(e.stderr)

root = RootUser(["sudo", "python3", "test.py"])
root.isRootUser()