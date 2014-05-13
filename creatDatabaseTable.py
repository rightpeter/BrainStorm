#!/usr/bin/env python
#encoding=utf-8

import db
from db import *
import tornado.database
import sys


def installRoomsTable():
    BrainDatabase.reconnect()
    BrainDatabase.execute("""CREATE TABLE `roomsTable`(
            `rid` INT NOT NULL AUTO_INCREMENT, 
            `lat` DOUBLE,
            `lng` DOUBLE,
            `name` VARCHAR(64), 
            `host` VARCHAR(64),
            `theme` text, 
            `range` double, 
            `max_num` int, 
            `pwflag` int,
            `password` VARCHAR(64),
            `time` int,
            `method` VARCHAR(64),
            `status` VARCHAR(64),
            `posttime` TIMESTAMP, 
            PRIMARY KEY(rid)) 
            DEFAULT CHARSET=utf8
    """)

    
def installIdeasTable():
    BrainDatabase.reconnect()
    BrainDatabase.execute("""CREATE TABLE `ideasTable`(
            `id` INT NOT NULL AUTO_INCREMENT,
            `rid` INT,
            `poster_name` VARCHAR(30),
            `content` text,
            PRIMARY KEY(id))
    """)

def installNewsTable():
    NewsDatabase.reconnect()
    NewsDatabase.execute("""CREATE TABLE `newsTable`(
            `id` INT NOT NULL AUTO_INCREMENT,
            `nid` INT NOT NULL,
            `publisher` VARCHAR(100),
            `sha1` VARCHAR(100),
            `date` VARCHAR(100),
            `title` text,
            `source` VARCHAR(100),
            `link` VARCHAR(100),
            `source_link` VARCHAR(100),
            `clean_body` text,
            `body` text,
            PRIMARY KEY(id))
            AUTO_INCREMENT=1000000
            DEFAULT CHARSET=utf8
    """)

def installUsersTable():
    BrainDatabase.reconnect()
    BrainDatabase.execute("""CREATE TABLE `usersTable`(
            `id` INT NOT NULL AUTO_INCREMENT,
            `email` VARCHAR(64),
            `name` VARCHAR(32) NOT NULL,
            `password` VARCHAR(512) NOT NULL,
            `last_login` timestamp,
            `lat` DOUBLE, 
            `lng` DOUBLE, 
            `subscribed` TINYINT(1) DEFAULT '1',
            `ext` VARCHAR(10),
            PRIMARY KEY(id),
            UNIQUE KEY`name`(`name`),
            UNIQUE KEY`email`(`email`))
            AUTO_INCREMENT=100000
            DEFAULT CHARSET=utf8
    """)

def installJoinTable():
    BrainDatabase.reconnect()
    BrainDatabase.execute("""CREATE TABLE `joinTable`(
            `rid` INT NOT NULL,
            `name` VARCHAR(64) NOT NULL,
            `join_time` timestamp,
            PRIMARY KEY(rid, name))
            DEFAULT CHARSET=utf8
    """)

def installCheckTable():
    NewsDatabase.reconnect()
    NewsDatabase.execute("""CREATE TABLE `checkTable`(
            `id` INT NOT NULL AUTO_INCREMENT,
            `email` VARCHAR(64) NOT NULL,
            `code` VARCHAR(64) NOT NULL,
            `check_time` timestamp,
            `checked` TINYINT(1) DEFAULT '0',
            PRIMARY KEY(id))
            DEFAULT CHARSET=utf8
    """)

def installSaltingTable():
    NewsDatabase.reconnect()
    NewsDatabase.execute("""CREATE TABLE `saltTable`(
            `email` VARCHAR(64) NOT NULL,
            `name` VARCHAR(32) NOT NULL,
            `salt` VARCHAR(64) NOT NULL,
            PRIMARY KEY(`name`))
            DEFAULT CHARSET=utf8
    """)

if __name__ == "__main__":
    # db.init_db()
    # models.kv.db_inited = ''
    if '-R' in sys.argv:
        installRoomsTable()

    if '-I' in sys.argv:
        installIdeasTable()

    if '-N' in sys.argv:
        installNewsTable()

    if '-U' in sys.argv:
        installUsersTable()

    if '-J' in sys.argv:
        installJoinTable()
        
    if '-CHECK' in sys.argv:
        installCheckTable()

    if '-SALT' in sys.argv:
        installSaltingTable()
