class Bootcamper:
    def __init__(self):
        self.bootcampers=[]
        self.e = 0
        self.p=0
        self.i=0
        self.c=0
        self.group=None
    def add_bootcamper(self,username,password):
        bootcampr={"username":username,
                    "password":password,
                    "group":self.group,
                    "scores":{"excellence":self.e,"passion":self.p,"integrity":self.i,"collaboration":self.c}
                    }
        return self.bootcampers.append(bootcampr)
    
    def rate_bootcamper(self,username,exc,pas,inte,coll):
        for bcmp in self.bootcampers:
            if bcmp['username']==username:
                for r in bcmp['scores']:
                    r['excellence']=exc
                    r['passion']=pas
                    r['integrity']=inte
                    r['collaboration']=coll
                return self.bcmp

    def add_bootcamper_to_group(self,username,group):
        for btc in self.bootcampers:
            if btc['username']==username:
                btc['group']=group
                return btc
    def bootcamper_login(self,username,password):
       for btc in self.bootcampers  
            if btc['username']==username and btc['password']==password:
                return btc['scores']
            
            else:
                return "wrong username or password"



    
