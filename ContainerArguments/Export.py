from lib.Argument import Argument
import sys
from lib.ContainerExport import ContainerExport
from lib.Window import Window
Arg = Argument(sys.argv)
from lib.Container import Container
window = Window()

def Export():
    if Arg.hasOptionValue('--containers'):
        listContainers = Arg.getoptionvalue('--containers')
        data = ContainerExport(listContainers).containerOutputData
        # print(data)
        for key, value in data.items():
            # print(value['isavailblecontainer'])
            status = value['status']
            name = value['name']
            isAvailbleContainer = value['isavailblecontainer']
            if isAvailbleContainer == 'yes':
                error = value['error']
                if error != None:
                    if status == 'success':
                        print(f'The container {name} has been successfully exported...')
                        # window.showInfoMessage(f'The container {name} has been successfully exported...')
                    
                else:
                    print(f'The container {name} has been failed exported...')
                    print(f"ERROR : {error}")
            else:
                print(f'Container {name} is not Available')  