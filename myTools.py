#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from datetime import *

from db import *
from math import *

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

def disAB(pos1, pos2):
    pos1[0] = 90 - pos1[0]
    pos2[0] = 90 - pos2[0]

    C = sin(pos1[0])*sin(pos2[0])*cos(pos1[1]-pos2[1])

    R = 6371.004
    Dis = R*acos(C)*pi/180

    return Dis 

def getNearby(pos, dis):
    BrainDatabase.reconnect()

    rooms_dic = BrainDatabase.query("""SELECT rid FROM roomsTable WHERE
        6371.004*ACOS(SIN(%s)*SIN(lat)*COS(%s-lng)+COS(%s)*COS(lat))*PI()/180 <
        %s""", pos[0], pos[1], pos[0], dis)

    rooms = []
    for k in rooms_dic:
        rooms.append(int(k['rid']))

    return rooms 

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

def matchBuildings(pic, buildings_list):
    return buildings_list[0]

class myTools:
    @classmethod
    def is_user_name_exist(self, name):
        name_sql = BrainDatabase.query("""SELECT name FROM usersTable WHERE
            name=%s""", name)
    
        if len(name_sql):
            return True 
        else:
            return False 

    @classmethod
    def is_room_name_exist(self, name):
        name_sql = BrainDatabase.query("""SELECT name FROM roomsTable WHERE
                name=%s""", name)

        if len(name_sql):
            return True
        else:
            return False

    @classmethod
    def is_room_id_exist(self, rid):
        rid_sql = BrainDatabase.query("""SELECT rid FROM roomsTable WHERE
            rid=%s""", rid)

        if len(rid_sql):
            return True
        else:
            return False

    @classmethod
    def is_user_in_room(self, name, rid):
        result = BrainDatabase.query("""SELECT * FROM joinTable WHERE rid=%s
                and name=%s""", rid, name)

        if len(result):
            return True
        else:
            return False

    @classmethod
    def insert_a_user(self, user):
        try:
            BrainDatabase.execute("""INSERT usersTable(`name`, `password`) VALUES(%s,
                %s)""", user['USER_NAME'], user['PASSWORD'])
            return True
        except Exception, e:
            print e
            return False

    @classmethod
    def insert_an_idea(self, idea):
        try:
            BrainDatabase.execute("""INSERT ideasTable(`rid`, `poster_name`,
                    `content`) VALUES(%s, %s, %s)""", idea['ROOM_ID'],
                    idea['POSTER_NAME'], idea['CONTENT'])
            return True
        except Exception, e:
            print e
            return False

    @classmethod
    def insert_a_room(self, room):
        try:
            BrainDatabase.execute("""INSERT roomsTable(`lat`, `lng`, `name`,
                `host`, `theme`, `range`, `max_num`, `pwflag`, `password`, `time`,
                `method`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                room['LAT'], room['LNG'], room['ROOM_NAME'], room['USER_NAME'], room['THEME'],
                room['RANGE'], room['MAX_NUM'], room['PWFLAG'],
                room['PASSWORD'], room['TIME'], room['METHOD'])        
            return True
        except Exception, e:
            print 'hehe', e 
            return False

    @classmethod
    def user_join_room(self, name, rid):
        try:
            BrainDatabase.execute("""INSERT joinTable(`rid`, `name`) VALUES(%s,
                    %s)""", rid, name)
            return True
        except Exception, e:
            print e
            return False
    
    @classmethod
    def login(self, name, password):
        if self.is_name_exist(name):
            password_sql = self.get_password_by_name(name)
            if password == password_sql:
                return True
            else:
                return False

    @classmethod
    def get_user_password_by_name(self, name):
        password = BrainDatabase.query("""SELECT password FROM usersTable WHERE
            name=%s""", name)[0]['password']
        return password

    @classmethod
    def get_room_password_by_id(self, rid):
        password = BrainDatabase.query("""SELECT password FROM roomsTable WHERE
                rid=%s""", rid)[0]['password']
        return password
    @classmethod
    def get_user_id_by_name(self, name):
        user_id = BrainDatabase.query("""SELECT id FROM usersTable WHERE
            name=%s""", name)
        if len(user_id):
            user_id = int(user_id[0]['id'])
        else:
            user_id = -1
        return user_id

    
    @classmethod
    def get_room_id_by_name(self, name):
        room_id = BrainDatabase.query("""SELECT rid FROM roomsTable WHERE
                name=%s""", name)
        if len(room_id):
            room_id = int(room_id[0]['rid'])
        else:
            room_id = -1
        return room_id

    @classmethod
    def get_room_idea_list(self, rid):
        idea_list_sql = BrainDatabase.query("""SELECT id FROM ideasTable WHERE
            rid=%s""", rid)
        idea_list = []
        for idea in idea_list_sql:
            idea_list.append(idea['id'])
        return idea_list

        
