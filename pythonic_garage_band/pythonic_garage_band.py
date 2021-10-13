class Musician():
    def __init__(self,members,name):
        self.members=members
        

class Band(Musician):
    def __init__(self,name):

        self.name=name

    def play_solos():
        pass    

class Guitarist(Band):
    
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"    


class Drummer(Band):
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"    
class Bassist:
    pass        