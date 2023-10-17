import hashlib
import random
import string

class Docker_ID:
    def __init__(self,Name):
        self.Name = Name
        hash_object = hashlib.new('sha256')
        hash_object.update(self.Name.encode('utf-8'))
        self.Id = hash_object.hexdigest()[:20]

    def ContainerId(self):
        return self.Id
    
    def ContainerName(self):
        return self.Name


# Docker_ID = Docker_ID('Sridhar')
# print(Docker_ID.ContainerName())
# print(Docker_ID.ContainerId())

