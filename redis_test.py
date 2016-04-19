#!/usr/bin/env python
# encoding: utf-8

import redis

# r=redis.StrictRedis(host='localhost',db=3)

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.port = 6379

    def write(self,website):