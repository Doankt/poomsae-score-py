class Competitor:
    def __init__(self, delim_name=''):
        self.delim_name = delim_name

    def __repr__(self):
        ret = 'Competitor({}, {})'
        sname = self.delim_name.split('~')
        return ret.format(sname[0], sname[1])