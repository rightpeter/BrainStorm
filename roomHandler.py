#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from db import *
from myTools import *

class RoomHandler(tornado.web.RequestHandler):
    def get(self, rid):
        rid = int(rid)
        detail = BrainDatabase.query("""SELECT * FROM roomsTable WHERE
                rid=%s""", rid)
        if len(detail):
            detail = detail[0]
        else:
            detail = {}

        idea_list = myTools.get_room_idea_list(rid)
        json_res = {'ROOM_ID': detail['rid'],
                    'ROOM_NAME': detail['name'],
                    'USER_NAME': detail['host'],
                    'THEME': detail['theme'],
                    'TIME': detail['time'],
                    'RANGE': detail['range'],
                    'METHOD': detail['method'],
                    'PWFLAG': detail['pwflag'],
                    'IDEA_LIST': idea_list}
        json_res = json.dumps(json_res)
        #encoded_json = json.dumps(detail, cls=CJsonEncoder) 
        self.write(json_res)
