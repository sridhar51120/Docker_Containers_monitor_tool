from lib.Argument import Argument
import sys
from lib.Docker_ID import Docker_ID
from lib.ContainerRename import ContainerRename
from lib.Window import Window
Arg = Argument(sys.argv)
from lib.Container import Container
container  = Container()
window = Window()

def Rename():
   # --container="{'sridhar':'sridha'}"
    if Arg.hasOptionValue('--containers'):
        Rename = Arg.getoptionvalue('--containers')
        data = ContainerRename(Rename).containerOutputData
        # print(data)
        for key, value in data.items():
            status = value['status']
            name = value['oldname']
            isAvailbleContainer = value['isavailblecontainer']
            if isAvailbleContainer == 'yes':
                isdeleted = value['olddata']
                if isdeleted == 'deleted':
                    if status == 'success':
                        print(f'The container {name} to {value["newname"]} has been successfully renamed....')
                    
                else:
                        print(f"failed to delete the data in the Users.json file {name} to {value['newname']}")   
            else:
                print(f'Container {name} is not Available')
        