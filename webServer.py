#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from tornado.options import define, options
from createRoomHandler import CreateRoomHandler
from queryRoomHandler import QueryRoomHandler
from roomHandler import RoomHandler
from signUpHandler import SignUpHandler
from signInHandler import SignInHandler
from postIdeaHandler import PostIdeaHandler
from ideaHandler import IdeaHandler
from joinHandler import JoinHandler
from acquireStatusHandler import AcquireStatusHandler
#from userHandler import UserHandler
#from urlMapHandler import UrlMapHandler

define("port", default=4358, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', MainHandler),
            (r'/createroom', CreateRoomHandler),
            (r'/room/(\d+)$', RoomHandler),
            (r'/signup', SignUpHandler),
            (r'/signin', SignInHandler),
            (r'/queryroom', QueryRoomHandler),
            (r'/postidea', PostIdeaHandler),
            (r'/idea/(\d+)$', IdeaHandler),
            (r'/join', JoinHandler),
            (r'/acquirestatus', AcquireStatusHandler),
            #(r'/user/(\d+)$', UserHandler),
            #(r'/urlmap', UrlMapHandler)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("Wo Shi Zhang Lu!")


def main():
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
