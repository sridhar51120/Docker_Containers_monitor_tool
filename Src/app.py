import sys
from lib.Argument import Argument
Arg = Argument(sys.argv)

from ContainerArguments.Create import Create
from ContainerArguments.Stop import Stop
from ContainerArguments.Restart import Restart
from ContainerArguments.Start import Start
from ContainerArguments.Remove import Remove
from ContainerArguments.Pause import Pause
from ContainerArguments.UnPause import UnPause
from ContainerArguments.Export import Export
from ContainerArguments.Logs import Logs
from ContainerArguments.Kill import Kill
from ContainerArguments.Prune import Prune
from ContainerArguments.Rename import Rename
from ContainerArguments.Top import Top

if Arg.hasCommands(['Container']):
    '''
    Command Usage : python app.py Container <containerAction> <{--name=ContainerName/--id=ContainerID}> 
    Options       :  
                    --options="{ContainerOptions}"  
                            Options Format ==> < --options="{'s':'1','se':'2'}" >
                            
                    --containers="['container1','container2'...]"  
                            Options Format ==> < --containers="['container1','container2'...]" >
    '''
    if Arg.hasCommands(['create']):
        Create()
          
    if Arg.hasCommands(['stop']):
        Stop()
                    
    if Arg.hasCommands(['restart']):
        Restart()
    
    if Arg.hasCommands(['start']):
        Start()
                
    if Arg.hasCommands(['remove']):
        Remove() 
         
    if Arg.hasCommands(['pause']):
        Pause()
       
    if Arg.hasCommands(['unpause']):
        UnPause()
    
    if Arg.hasCommands(['export']):
        Export()
                    
    if Arg.hasCommands(['logs']):
        Logs()
    
    if Arg.hasCommands(['kill']):
        Kill()
    
    if Arg.hasCommands(['prune']):
        Prune()
            
    if Arg.hasCommands(['rename']):
        Rename()
        
    if Arg.hasCommands(['top']):
        Top()