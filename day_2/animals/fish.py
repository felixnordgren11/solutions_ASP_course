



class Fish:
    def __init__(self):
        ''' Constructor for this class. '''
        self.members = ['Shark', 'Tuna', 'Salmon']


    def printMembers(self):
        for member in self.members:
            print('\t%s ' % member)