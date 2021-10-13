class Musician():
    def __init__(self,members,name):
        self.members=members
        

class Band(Musician):
    def __init__(self,name,members):

        self.name=name
        self.members=members
    def play_solos():
        pass  
    # def get_instrument(self): 
    #     return self.members  

class Guitarist(Musician):
    
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"    
    def get_instrument(self):
        return "guitar"

class Drummer(Musician):
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"    
    def get_instrument(self): 
        return "drums"
class Bassist(Musician):
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"  
    def get_instrument(self): 
        return "bass"