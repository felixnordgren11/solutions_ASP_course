from .birds import Birds
from .mammals import Mammals
from .fish import Fish


class Birds():
    def __init__(self):
        ''' Constructor for this class. '''
        self.members = ['Robin', 'Duck']



    def printMembers(self):
        for member in self.members:
            print('\t%s ' % member)



class Mammals():
    def __init__(self):
        ''' Constructor for this class. '''
        self.members = ['Elephant']


        
    def printMembers(self):
        for member in self.members:
            print('\t%s ' % member)


class Fish():
    def __init__(self):
        ''' Constructor for this class. '''
        self.members = ['Tuna', 'Salmon']


        
    def printMembers(self):
        for member in self.members:
            print('\t%s ' % member)
