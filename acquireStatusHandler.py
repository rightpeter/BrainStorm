#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from db import *
from myTools import *

class AcquireStatusHandler(tornado.web.RequestHandler):
    def post(self):
        jsonDict = json.loads(self.request.body)
        print jsonDict
        
        json_res = {}
        if myTools.is_user_in_room(jsonDict['USER_NAME'], jsonDict['ROOM_ID']):
            json_res['USER_STATUS'] = 'IN'
        else:
            json_res['USER_STATUS'] = "OUT"

        room_status = BrainDatabase.query("""SELECT status FROM
            roomsTable WHERE rid=%s""", jsonDict['ROOM_ID'])
        if len(room_status):
            room_status = room_status[0]['status']
        else:
            room_status = "NULL"

        json_res['ROOM_STATUS'] = room_status
        json_res = json.dumps(json_res)
        self.write(json_res)
