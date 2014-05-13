#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from db import *
from myTools import *

class IdeaHandler(tornado.web.RequestHandler):
    def get(self, iid):
        iid = int(iid)         
        detail = BrainDatabase.query("""SELECT * FROM ideasTable WHERE id=%s""",
               iid)
        if len(detail):
           detail = detail[0]
        else:
            detail = {}

        json_res = {'CONTENT': detail['content'],
                    'POSTER_NAME': detail['poster_name']}

        json_res = json.dumps(json_res)
        self.write(json_res)
