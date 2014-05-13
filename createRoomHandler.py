#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from db import *
from myTools import *

class CreateRoomHandler(tornado.web.RequestHandler):
    def post(self):
        raw_body = str(self.request.body)
        room = json.loads(raw_body)
        print room

        if not myTools.is_room_name_exist(room['ROOM_NAME']) and myTools.is_user_name_exist(room['USER_NAME']):
            print "insert!"
            if myTools.insert_a_room(room):
                room_id = myTools.get_room_id_by_name(room['ROOM_NAME'])
                json_res = {"ROOM_ID": room_id}
                json_res = json.dumps(json_res)
                self.write(json_res)
                return 

        json_res = {"ROOM_ID": -1}
        json_res = json.dumps(json_res)
        self.write(json_res)
