import json

class User:
    def newUser(self,name,json_file_path):
        try:
            with open(json_file_path, 'r') as file:
                fileData = json.load(file)
            file.close()
            if name in fileData:
                # return True
                # TODO: Change the User Privillages 
                return False
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
        
