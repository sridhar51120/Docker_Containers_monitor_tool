from lib.Argument import Argument
from lib.Dashboard import Dashboard
import json
import os
import sys

 
Arg = Argument(sys.argv)
       
def addUser(data, json_file_path="data.json"):
    try:
        if json_file_path and json_file_path.strip() and len(json_file_path.strip()) > 0:
            with open(json_file_path, 'r') as file:
                existing_data = json.load(file)

        else:
            existing_data = []
        existing_data.append(data)

        with open(json_file_path, 'w') as file:
            json.dump(existing_data, file, indent=4)
        return True

    except json.JSONDecodeError as e:
        print(f"Invalid JSON format in the JSON file: {json_file_path}")
        return False

    except Exception as e:
        print("An error occurred:", str(e))
        return False


# try:
if Arg.hasCommands(['Container']):
    if Arg.hasCommands(['Create']) and Arg.hasOptionValue('--name'):
        Dashboard = Dashboard(Arg.getoptionvalue('--name'))
        id = Dashboard.Container_Id()
        name = Dashboard.ContainerName()
        addUser({name: id})

    elif Arg.hasOption(['--list']):
        print("list")

    elif Arg.hasOptionValue('--name') and Arg.hasOption(['--info']):
        Dashboard = Dashboard(Arg.getoptionvalue('--name'))
        info = Dashboard.ContainerInfo()
        print(json.dumps(info, indent = 4))

    elif Arg.hasOption(['--list']):
        print("List the Containers list")
            

# except:
#     print("Error")


# Dashboard = Dashboard("sridhar")
# print(Dashboard.ContainerInfo())

