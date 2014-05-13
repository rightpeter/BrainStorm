#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from db import *
from myTools import *

class SignUpHandler(tornado.web.RequestHandler):
    def post(self):
        jsonDic = json.loads(self.request.body)
        print jsonDic
        if jsonDic['PASSWORD'] == jsonDic['REPASSWORD']:
            if not myTools.is_user_name_exist(jsonDic['USER_NAME']):
                #print "not excist"
                if myTools.insert_a_user(jsonDic):
                    user_id = myTools.get_user_id_by_name(jsonDic['USER_NAME'])
                    json_res = {"USER_ID": user_id}
                    json_res = json.dumps(json_res)
                    self.write(json_res)
                    return

        json_res = {"USER_ID": -1}
        json_res = json.dumps(json_res)
        self.write(json_res)
