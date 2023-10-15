import json
import sys
import ast
from lib.Argument import Argument 
Arg = Argument(sys.argv)

class Container:
    def ContainerId(self,json_file_path):
        try:
            if Arg.hasOptionValue('--name') or Arg.hasOptionValue('--id'):
                if Arg.hasOptionValue('--name'):
                    with open(json_file_path, 'r') as file:
                        fileData = json.load(file)
                        file.close()
                        name = Arg.getoptionvalue('--name')
                        # print(name)
                        if name in fileData:
                            return fileData[name]
                        else:
                            return False
                            # TODO: retrun False
                            # raise Exception("Username is Not Registered..Please check your Container Name")
                if Arg.hasOptionValue('--id'):
                    return Arg.getoptionvalue('--id')
            else:
                return False
        except Exception as e:
            print(f'Exception {e}')
            
    def ContainerName(self,json_file_path):
        try:
            if Arg.hasOptionValue('--name'):
                return Arg.getoptionvalue('--name')
            
            if Arg.hasOptionValue('--id'):
                id = Arg.getoptionvalue('--id')
                with open(json_file_path, 'r') as file:
                    fileData = json.load(file)
                    file.close()
                    for data in fileData.items():
                        if data[1] == id:
                            return str(data[0])
                    
        except Exception as e:
            print(f'Exception {e}')

    def UserContainerOptionCommand(self,command,userOption=None):
        # --options="{'s':'1','se':'2'}"
        if userOption != None:
            options = ast.literal_eval(userOption)
            for option in options.items():
                command.append(option[0])
                command.append(option[1])
            return command
                
        elif userOption == None: 
            return command
    
    
    # def listContainers(self,command,containers):
    #     containers = ast.literal_eval(containers)
    #     for container in containers:
    #         command.append(container)
    #     return command
    