#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from db import *
from myTools import *

class QueryRoomHandler(tornado.web.RequestHandler):
    def post(self):
        jsonDict = json.loads(self.request.body)
        print jsonDict

        try:
            room_list = getNearby((jsonDict['LAT'], jsonDict['LNG']), jsonDict['RANGE']) 
            print room_list
            json_res = {'ROOM_LIST': room_list}
        except:
            json_res = {'ROOM_LIST': -1}
        finally:
            json_res = json.dumps(json_res)
            self.write(json_res)
