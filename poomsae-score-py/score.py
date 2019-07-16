import random

MAX_ACCURACY = 4.0
MAX_PRESENTATION = 6.0

def _valid_accuracy(a: float):
    return 0 <= a <= MAX_ACCURACY

def _valid_presentation(p: float):
    return 0 <= p <= MAX_PRESENTATION

class Score:
    def __init__(self, a: float = 0.0, p: float = 0.0):
        if _valid_accuracy(a): self.accuracy = a
        else:   raise ValueError("Accuracy a= {} is out of bounds".format(a))
        
        if _valid_presentation(p): self.presentation = p
        else:   raise ValueError("Presentation p= {} is out of bounds".format(p))
    
    def total_avg(self):
        return round(self.accuracy + self.presentation, 1)
    
    def __repr__(self):
        ret = 'Score({}, {})'
        return ret.format(str(self.accuracy), str(self.presentation))


def gen_random_score():
    return Score(round(random.random() * MAX_ACCURACY, 1), round(random.random() * MAX_PRESENTATION, 1))

