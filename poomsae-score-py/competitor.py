class Competitor:
    def __init__(self, fn = '', ln = ''):
        self.first_name = fn
        self.last_name = ln
        
    def __repr__(self):
        return self.first_name + ' ' + self.last_name