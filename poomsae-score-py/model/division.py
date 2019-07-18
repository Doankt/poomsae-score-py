from collections import OrderedDict
import random
import json

# import fullscore


class Division:
    def __init__(self, d_name, ring_number=-1):
        self.__type__ = 'Division'
        self.division_name = d_name
        self.ring_number = ring_number
        self.full_score_list = OrderedDict()

    def add_competitor(self, competitor):
        self.full_score_list[competitor] = None

    def set_score(self, competitor, fs):
        if competitor in self.full_score_list:
            self.full_score_list[competitor] = fs

    def contains_id(self):
        return '_id' in self.__dict__

    def gen_random_order(self):
        return random.sample(self.full_score_list.keys(), k=len(self.full_score_list))