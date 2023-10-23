import subprocess
import ast
from lib.User import User
from lib.Container import Container
Container = Container()

class ContainerPrune:
    def __init__(self):
        self.containerOutputData = {}
        self.ContainerPrune = self.ContainerPrune()

    def ContainerPrune(self):
        command = ["docker","container","prune"]
        result = subprocess.run(command, capture_output=True, text=True)
        print(result)
        # if result.stderr != None:
        #     data = {}
        #     data['isavailblecontainer'] = 'yes'
        #     data['returncode'] = result.returncode
        #     data['status'] = 'success'
        #     data['error'] = result.stderr
        #     data['stdout'] = result.stdout
        #     self.containerOutputData[index] = data
        # else:
        #     data = {}
        #     data['isavailblecontainer'] = 'yes'
        #     data['returncode'] = result.returncode
        #     data['status'] = 'fail'
        #     data['error'] = result.stderr
        #     data['stdout'] = result.stdout
        #     self.containerOutputData[index] = data
        
        return self.containerOutputData
    