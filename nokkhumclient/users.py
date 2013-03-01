'''
Created on Feb 27, 2013

@author: boatkrap
'''
from . import base

class User(base.Resource):
    pass

class UserManager(base.Manager):
    resource_class = User
    