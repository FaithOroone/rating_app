class Bootcamper:
    def __init__(self):
        self.bootcampers=[]
    def add_bootcamper(self,username,password):
        bootcampr={"username":username,
                    "password":password
                    }
        return self.bootcampers.append(bootcampr)
    
