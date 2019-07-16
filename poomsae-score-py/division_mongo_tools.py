import json

import pymongo
import bson
from division import Division
from competitor import Competitor
from score import Score
from fullscore import FullScore


def psdiv_load(file):
    with open(file, 'r') as json_file:
        data = json.loads(json_file.read())

        if '__type__' in data and data['__type__'] == 'Division':
            ret = Division(data['divisionName'], data['ringNumber'])
            ret.date = data['date']

            fsl = data['fullScoreList']
            for name in fsl:
                cmp = Competitor(name)
                ret.add_competitor(cmp)

                score_list = fsl[name]
                if score_list:
                    ret.set_score(cmp, FullScore(len(score_list), score_list))
            return ret
    raise TypeError('File is not __type__: Division')


def _psdiv_encode(division):
    ret = division.__dict__.copy()
    temp_fsl = dict()
    for comp, fs in ret['full_score_list'].items():
        if fs:
            temp_fsl[comp.delim_name] = [[score.accuracy, score.presentation] for score in fs.score_list]
        else:
            temp_fsl[comp.delim_name] = None

    ret['full_score_list'] = temp_fsl
    return ret


def upload_division(division):
    enco = _psdiv_encode(division)

    client = pymongo.MongoClient(
        "mongodb+srv://doankt:Buy1get1free@poomsaescore-rpi4g.mongodb.net/test?retryWrites=true&w=majority")
    working_db = client['tournaments']
    working_collection = working_db['Test Tournament']

    res = working_collection.insert_one(enco)
    print(res.inserted_id)
    return bson.objectid.ObjectId(res.inserted_id)
