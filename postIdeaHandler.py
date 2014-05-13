#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from db import *
from myTools import *

class PostIdeaHandler(tornado.web.RequestHandler):
    def post(self):
        jsonDict = json.loads(self.request.body)
        print jsonDict

        if myTools.is_user_in_room(jsonDict['POSTER_NAME'], jsonDict['ROOM_ID']):
            if myTools.insert_an_idea(jsonDict):
                json_res = {"STATUS": "SUCCESS"}
                json_res = json.dumps(json_res)
                self.write(json_res)
                return

        json_res = {"STATUS": "ERROR"}
        json_res = json.dumps(json_res)
        self.write(json_res)

