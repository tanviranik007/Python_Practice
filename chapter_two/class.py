class Human:
    def __init__(self,n,o):
        self.name = n
        self.occupation=o
        
    def do_work(self):
        if self.occupation=="tennis Player":
            print(self.name, "plays tennis")
        elif self.occupation=="actor":
            print(self.name,"shoots a flim")
            
    def speaks(self):
        print(self.name,"says how are You?")
        
        
tom=Human("tom cruise","actor")
tom.do_work()
tom.speaks()
        