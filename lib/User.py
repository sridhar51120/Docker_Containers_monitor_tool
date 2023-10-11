import json
import sys
import ast
from lib.Argument import Argument 
Arg = Argument(sys.argv)

class User:
    def newUser(self,name,id, json_file_path):
        try:
            with open(json_file_path, 'r') as file:
                fileData = json.load(file)
            file.close()
            if name in fileData:
                return True
                # TODO: Change the User Privillages 
                # return False
            else:
                return True
        except json.JSONDecodeError as e:
            print(f"Invalid JSON format in the JSON file: {json_file_path}")
            return False  

    def addUser(self,name,id, json_file_path):
        try:
            with open(json_file_path, 'r') as file:
                fileData = json.load(file)
                file.close()

            fileData[name] = id
            data = json.dumps(fileData, indent=4)

            with open(json_file_path, 'w') as file:
                file.write(data)
                file.close()
                return id
            
        except json.JSONDecodeError as e:
            print(f"Invalid JSON format in the JSON file: {json_file_path}")
            return False
        
    def ContainerId(self,json_file_path):
        try:
            if Arg.hasOptionValue('--name'):
                with open(json_file_path, 'r') as file:
                    fileData = json.load(file)
                    file.close()
                    name = Arg.getoptionvalue('--name')
                    # print(name)
                    if name in fileData:
                        return fileData[name]
                    else:
                        raise Exception("Username is Not Registered..Please check your Container Name")
            if Arg.hasOptionValue('--id'):
                return Arg.getoptionvalue('--id')
        except Exception as e:
            print(f'Exception {e}')
            

    def ContainerName(self,json_file_path):
        try:
            if Arg.hasOptionValue('--name'):
                return True,Arg.getoptionvalue('--name')
            
            if Arg.hasOptionValue('--id'):
                id = Arg.getoptionvalue('--id')
                with open(json_file_path, 'r') as file:
                    fileData = json.load(file)
                    file.close()
                    for data in fileData.items():
                        if data[1] == id:
                            return True,str(data[0])
                    
        except Exception as e:
            print(f'Exception {e}')

    def UserContainerOption(self,userOption):
        options = userOption.replace("'", "\"")
        options = userOption.replace("'", "\"")
        options_dict = ast.literal_eval(options)
        options_str = ''
        for i in options_dict.items():
            options_str = options_str + f"'{i[0]}','{i[1]}',"
            
        return options_str