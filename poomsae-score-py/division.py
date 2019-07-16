from collections import OrderedDict

import random
import fullscore
import csv


class Division:
    def __init__(self, d_name):
        self.division_name = d_name
        self.full_score_list = OrderedDict()
        
    def add_competitor(self, competitor):
        self.full_score_list[competitor] = None
    
    def set_score(self, competitor, fs):
        if competitor in self.full_score_list:
            print('g')
            self.full_score_list[competitor] = fs

    def gen_random_order(self):
        return random.sample(self.full_score_list.keys(), k=len(self.full_score_list))