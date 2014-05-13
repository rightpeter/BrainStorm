#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from db import *
from myTools import *

class SignInHandler(tornado.web.RequestHandler):
    def post(self):
        jsonDic = json.loads(self.request.body)
        print jsonDic
        
        if myTools.login(jsonDic['USER_NAME'], jsonDic['PASSWORD']):
            BrainDatabase.execute("""UPDATE usersTable SET lat=%s, lng=%s WHERE
                    name=%s""", jsonDic['LAT'], jsonDic['LNG'],
                    jsonDic['USER_NAME'])
            user_id = myTools.get_user_id_by_name(jsonDic['USER_NAME'])
            json_res = {'USER_ID': user_id}
            json_res = json.dumps(json_res)
            self.write(json_res)
        else:
            json_res = {'USER_ID': -1}
            json_res = json.dumps(json_res)
            self.write(json_res)
