class Window:
    def showInfoMessage(self,info):
       try:  
        return f'\033[92m{info}\033[0m'
       except Exception as e:
           return e
    
    def showErrorMessage(self,info):
        try:
            return f'\033[91m{info}\033[0m'  
        except Exception as e:
            return e
    
    def showWarningMessage(self,info):
        try:
            return f'\033[33m{info}\033[0m'
        except Exception as e:
            return e