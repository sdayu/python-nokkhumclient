'''
Created on Mar 1, 2013

@author: boatkrap
'''

from . import base

class CameraOperating(base.Resource):
    pass


class CameraOperatingManager(base.Manager):
    resource_class = CameraOperating
    
    def get(self, camera_id):
        return self._get('/cameras/%s/operating'%str(camera_id), "camera_operating")
    
    def update(self):
        pass