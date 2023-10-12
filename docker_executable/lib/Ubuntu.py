import shutil
class Ubuntu:
    def __init__(self,path=None):
        self.path = self.find_docker_executable
        
    def find_docker_executable():
        docker_executable = shutil.which('docker')
        return docker_executable
    

