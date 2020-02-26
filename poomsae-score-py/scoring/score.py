import random

MAX_ACCURACY = 4.0
MAX_PRESENTATION = 6.0

def _valid_accuracy(a: float):
    return a is None or 0 <= a <= MAX_ACCURACY

def _valid_presentation(p: float):
    return p is None or 0 <= p <= MAX_PRESENTATIO

class Score:
    def __init__(self, a: float = None, p: float = None):
        if _valid_accuracy(a): self.accuracy = a
        else:   raise ValueError("Accuracy a= {} is out of bounds".format(a))
        
        if _valid_presentation(p): self.presentation = p
        else:   raise ValueError("Presentation p= {} is out of bounds".format(p))
    
    def total_avg(self):
        if self.accuracy is None:   a = 0.0
        else:   a = self.accuracy

        if self.presentation is None: p = 0.0
        else: p = self.presentation

        return round(a + p, 1)

    def complete_state(self):
        #0 none
        #1 acc
        #2 pres
        if self.accuracy is None and self.presentation is None:
            return 0
        elif self.accuracy is not None and self.presentation is None:
            return 1
        else:
            return 2

    def __repr__(self):
        ret = 'Score({}, {})'
        return ret.format(str(self.accuracy), str(self.presentation))


def gen_random_score():
    return Score(round(random.random() * MAX_ACCURACY, 1), round(random.random() * MAX_PRESENTATION, 1))

