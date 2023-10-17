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
            
    def ContainerName(self,id,json_file_path):
        try:
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
    
    def CovertOutputTextFile(self,logs,filename,type):
        if type == 'logs':
            filename = filename + "_logs_file.txt"
            with open(filename, "w") as text_file:
                text_file.write(logs)
            return True
        
        elif type == 'process':
            filename = filename + "_process_file.txt"
            with open(filename, "w") as text_file:
                text_file.write(logs)
                
            return True

    def RemoveContainer(self,oldContainerName,json_file_path):
        try:
            with open(json_file_path, 'r') as file:
                data = json.load(file)
            if oldContainerName in data:
                del data[oldContainerName]
            with open(json_file_path, 'w') as file:
                json.dump(data, file, indent=4)
                return True

        except Exception as e:
            return e
                    