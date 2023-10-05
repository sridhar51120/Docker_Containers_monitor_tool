from lib.Argument import Argument
from lib.Dashboard import Dashboard
import sys

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
            print(info)

except:
    print("Error")


# Dashboard = Dashboard("sridhar")
# print(Dashboard.Container_Id())

