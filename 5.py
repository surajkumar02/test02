class Student:
    def __init__(self,name,phy,chem,bio):
        self.name=name
        self.phy=phy
        self.chem=chem
        self.bio=bio


    
    def Total(self):
        return (self.phy+self.chem+self.bio)

    def Percentage(self):
        return (((self.phy+self.chem+self.bio)/300)*100)