#!/usr/bin/env python
#encoding=utf-8
'''db'''
import config
import tornado.database

BrainDatabase = tornado.database.Connection(
    "127.0.0.1:3306",
    "BrainStorm",
    "pedestal",
    "cippusrightpeter",
)
