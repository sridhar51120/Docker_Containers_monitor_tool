import json
import sys
import ast
from lib.Argument import Argument 
Arg = Argument(sys.argv)

class Container:
    def ContainerId(self,containerName,json_file_path):
        try:
            with open(json_file_path, 'r') as file:
                fileData = json.load(file)
                file.close()
            
                if containerName in fileData:
                    return fileData[containerName]
                else:
                    return False
                    # TODO: retrun False
                    # raise Exception("Username is Not Registered..Please check your Container Name")
                
        except Exception as e:
            print(f'Exception {e}')
            
    # def ContainerName(self,json_file_path):
    #     try:
    #         if Arg.hasOptionValue('--name'):
    #             return Arg.getoptionvalue('--name')
            
    #         if Arg.hasOptionValue('--id'):
    #             id = Arg.getoptionvalue('--id')
    #             with open(json_file_path, 'r') as file:
    #                 fileData = json.load(file)
    #                 file.close()
    #                 for data in fileData.items():
    #                     if data[1] == id:
    #                         return str(data[0])
                    
    #     except Exception as e:
    #         print(f'Exception {e}')

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
    
    def createLogFile(self,logs,filename):
        filename = filename + "_logs_file.txt"
        with open(filename, "w") as text_file:
            text_file.write(logs)
            
        return True