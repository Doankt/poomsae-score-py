import json
from bson.objectid import ObjectId
import pymongo
from passlib.hash import argon2
from validate_email import validate_email



import exceptions
from model.division import Division
from model.competitor import Competitor
from model.fullscore import FullScore

USER_MNGR_USER = 'userManager'
USER_MNGR_PASSWD = 'mg1ImFbYgdYRi9gt'

# TEMP_API_KEY ='61762a77-af25-4b2c-9cc1-0dc2df4e8ee8'

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


# Change to update
def upload_division(division):
    enco = _psdiv_encode(division)

    client = pymongo.MongoClient(
        "mongodb+srv://{username}:{password}@poomsaescore-rpi4g.mongodb.net/test?retryWrites=true&w=majority".format(
            username='doankt',
            password='Buy1get1free'
        ))
    working_db = client['tournaments']
    working_collection = working_db['Test Tournament']

    res = working_collection.insert_one(enco)
    print(res.inserted_id)
    return ObjectId(res.inserted_id)

def create_user(username, email, passwd):
    client = pymongo.MongoClient(
        "mongodb+srv://{username}:{password}@poomsaescore-rpi4g.mongodb.net/test?retryWrites=true&w=majority".format(
            username=USER_MNGR_USER,
            password=USER_MNGR_PASSWD))
    users_db = client['users']
    users_collection = users_db['tournamentAdmins']

    if tadmin_collection.count_documents({'email': email}): raise exceptions.EmailAlreadyExists(email)
    if tadmin_collection.count_documents({'user': username}): raise exceptions.UserAlreadyExists(username)
    if not validate_email(email): raise exceptions.InvalidEmail(email)

    users_collection.insert_one({'email': email, 'username': username, 'hashed_password': argon2.hash(passwd)})


def login_authenticate(username, passwd):
    client = pymongo.MongoClient(
        "mongodb+srv://{username}:{password}@poomsaescore-rpi4g.mongodb.net/test?retryWrites=true&w=majority".format(
            username=USER_MNGR_USER,
            password=USER_MNGR_PASSWD))
    users_db = client['users']
    users_collection = users_db['tournamentAdmins']

    doc = users_collection.find_one({'username': username})
    print(doc)
    if not doc: raise exceptions.UserDoesNotExist

    return argon2.verify(passwd, doc['hashed_password'])

