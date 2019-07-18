import model.score

MAX_JUDGES = 7;
DEFAULT_NUM_JUDGES = 5;

def _valid_num_judges(num_judges: int):
    return 0 < num_judges < MAX_JUDGES

class FullScore:
    def __init__(self, num_judges: int = 5, score_list=[]):
        if _valid_num_judges(num_judges): self.num_judges = num_judges
        else: raise ValueError("num_judges= {} is out of bounds".format(num_judges))

        if(score_list):
            self.score_list = [model.score.Score(s[0], s[1]) for s in score_list]
        else:
            for i in range(num_judges):
                self.score_list.append(None)
        
        print(self.score_list)
    
    def set_score(self, i:int, s: model.score.Score):
        if 0 <= i < len(self.score_list):  self.score_list[i] = s
        else: raise IndexError()
        
    
    def avg_accuracy(self):
        ret = 0.0
        num_valid = 0
        
        for s in self.score_list:
            if(s):
                ret += s.accuracy
                num_valid += 1
        
        if num_valid == 0:  return 0.0
        return round(ret / num_valid, 3)
    
    def avg_presentation(self):
        ret = 0.0
        num_valid = 0
        
        for s in self.score_list:
            if(s):
                ret += s.presentation
                num_valid += 1
        
        if num_valid == 0:  return 0.0
        return round(ret / num_valid, 3)
    
    def total_accuracy(self):
        ret = 0.0

        for s in self.score_list:
            if(s):
                ret += s.accuracy
        
        return round(ret, 1)
    
    def total_presentation(self):
        ret = 0.0

        for s in self.score_list:
            if(s):
                ret += s.presentation
        
        return round(ret, 1)
    
    def total_avg(self):
        ret = 0.0
        num_valid = 0
        
        for s in self.score_list:
            if(s):
                ret += s.total_avg()
                num_valid += 1
                
        if num_valid == 0:  return 0.0
        return round(ret / num_valid, 3)
    
    def __repr__(self):
        ret = 'FullScore(total_avg={})'
        return ret.format(self.total_avg())
                
    
def gen_random_fullscore(num_judges):
    ret = FullScore(num_judges)
    
    for i in range(num_judges):
        ret.set_score(i, model.score.gen_random_score())
    
    return ret
