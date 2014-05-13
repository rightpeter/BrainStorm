#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from db import *
from myTools import *

class JoinHandler(tornado.web.RequestHandler):
    def post(self):
        jsonDict = json.loads(self.request.body)
        print jsonDict
            
        if myTools.is_room_id_exist(jsonDict['ROOM_ID']) and\
           myTools.is_user_name_exist(jsonDict['USER_NAME']) and\
           not myTools.is_user_in_room(jsonDict['USER_NAME'], jsonDict['ROOM_ID']) and \
           myTools.get_room_password_by_id(jsonDict['ROOM_ID']) == jsonDict['PASSWORD']:
            if myTools.user_join_room(jsonDict['USER_NAME'], jsonDict['ROOM_ID']):
                json_res = {"STATUS": "OK"}
                json_res = json.dumps(json_res)
                self.write(json_res)
                return 

        json_res = {"STATUS": "ERROR"}
        json_res = json.dumps(json_res)
        self.write(json_res)
