from collections import OrderedDict

import random
import fullscore
import json



class Division:
    def __init__(self, d_name, ring_number=1):
        self.division_name = d_name
        self.ring_number = ring_number
        self.full_score_list = OrderedDict()

    def add_competitor(self, competitor):
        self.full_score_list[competitor] = None

    def set_score(self, competitor, fs):
        if competitor in self.full_score_list:
            self.full_score_list[competitor] = fs

    def gen_random_order(self):
        return random.sample(self.full_score_list.keys(), k=len(self.full_score_list))