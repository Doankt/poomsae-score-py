import random

MAX_ACCURACY = 4.0
MAX_PRESENTATION = 6.0

def _valid_accuracy(a: float):
    return a is None or 0 <= a <= MAX_ACCURACY

def _valid_presentation(p: float):
    if p is None: return True
    if len(p) != 3: return False
    for i in range(3):
        if p[i] is None or p[i] < 0 or p[i] > 2.0:
            return False
    return True

class Score:
    def __init__(self, a: float = None, p: list = None):
        if _valid_accuracy(a): self.accuracy = a
        else:   raise ValueError("Accuracy a= {} is out of bounds".format(a))
        
        if _valid_presentation(p): self.presentation = p
        else:   raise ValueError("Presentation p= {} is out of bounds".format(p))
    
    def total_avg(self):
        if self.accuracy is None:   a = 0.0
        else:   a = self.accuracy

        if self.presentation is None: p = [0.0, 0.0, 0.0]
        else: p = self.presentation

        print(round(a + sum(p), 1))
        return round(a + sum(p), 1)

    def get_acc(self):
        if self.accuracy is not None:
            return self.accuracy
        return 0.0

    def get_total_pres(self):
        if self.presentation is not None:
            return sum(self.presentation)
        return 0.0

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

