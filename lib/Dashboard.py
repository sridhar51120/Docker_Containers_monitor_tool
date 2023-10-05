from lib.Docker_ID import Docker_ID

class Dashboard:
    def __init__(self,name,image=None,status=None,port=None,resource_limit = None,health_status = None,logs = None):
        self.Name = name
        self.Id = Docker_ID(self.Name).ContainerId()
        self.Image = "Ubuntu 22.03"
        self.status = "Running" # TODO:Collect the Status
        self.port = "8080" # TODO: Collect the Port Details
        self.resource_limit = {
            "Cpu_percentage" : "0.7%",
            "Mem/Per_limit" : "796 KB / 64 MB",
            "Mem_percentage" : "0.1%"

        }  # TODO: Collect the Resource Limit CPU and Memory in {}
        self.health_status = "Good" # TODO: Collect  the Health Status
        self.logs = "This is a Sample Container logs" # TODO: Collect the Container logs and Convert to file and Save the Desired DIR
        self.Data = {} 
         
    def Container_Id(self):
        return self.Id

    def ContainerName(self):
        return self.Name

    def ContainerInfo(self):
        self.Data['Container Name'] = self.Name
        self.Data['Container ID'] = self.Id
        self.Data['Image'] = self.Image
        self.Data['Status'] = self.status
        self.Data['Port'] = self.port
        self.Data['Resource Limits'] = self.resource_limit
        self.Data['Health Status'] = self.health_status
        self.Data['Logs'] = self.logs
        return self.Data

