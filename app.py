from lib.Argument import Argument
from lib.Dashboard import Dashboard
import sys
import json

# Container name with id


Arg = Argument(sys.argv)

try:
    if Arg.hasCommands(['Container']):
        if Arg.hasCommands(['Create']) and Arg.hasOptionValue('--name'):
            Dashboard = Dashboard(Arg.getoptionvalue('--name'))
            id = Dashboard.Container_Id()
            name = Dashboard.ContainerName()
            print(name)
            print(id)

        elif Arg.hasOption(['--list']):
            print("list")

        elif Arg.hasOptionValue('--name') and Arg.hasOption(['--info']):
            Dashboard = Dashboard(Arg.getoptionvalue('--name'))
            info = Dashboard.ContainerInfo()
            print(json.dumps(info, indent = 4))

        elif Arg.hasOption(['--list']):
            

except:
    print("Error")


# Dashboard = Dashboard("sridhar")
# print(Dashboard.ContainerInfo())

