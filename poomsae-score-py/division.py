import fullscore

class Division:
    def __init__(self, d_name):
        self.division_name = d_name
        self.full_score_list = dict()
        
    def add_competitor(self, competitor):
        self.full_score_list[competitor] = None
    
    def set_score(self, competitor, fs):
        if competitor in self.full_score_list:
            print('g')
            self.full_score_list[competitor] = fs
        
        