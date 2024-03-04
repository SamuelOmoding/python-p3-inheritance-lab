#!/usr/bin/env python

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    pass



user = User('Juma', 'TheQue')
print(user.first_name)
print(user.last_name)