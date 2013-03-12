'''
Created on Mar 6, 2013

@author: boatkrap
'''
from .. import base

from .. import users
from .. import cameras

class CameraCommandQueue(base.Resource):
    @property
    def owner(self):
        return users.User(self.manager.api.users, self._info['owner'])

    @property
    def camera(self):
        return cameras.Camera(self.manager.api.cameras, self._info['camera'])
    
class CameraCommandQueueManager(base.Manager):
    resource_class = CameraCommandQueue
    
    def list(self):
        return self._list('/admin/camera_command_queue', 'camera_command_queue')
    
    def get(self, command_id):
        return self._get('/admin/camera_command_queue/%s'%str(command_id), 'camera_command')