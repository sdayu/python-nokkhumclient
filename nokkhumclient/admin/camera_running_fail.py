'''
Created on Mar 6, 2013

@author: boatkrap
'''
from .. import base

from .. import users
from .. import cameras
from . import compute_nodes

class CameraRunningFail(base.Resource):
    pass
#    @property
#    def owner(self):
#        return users.User(self.manager.api.users, self._info['owner'])
#
    @property
    def camera(self):
        return cameras.Camera(self.manager.api.cameras, self._info['camera'])
    
    @property
    def compute_node(self):
        if 'compute_node' in self._info:
            return compute_nodes.ComputeNode(self.manager.api.admin.compute_nodes, self._info['compute_node'])
        return None
    

class CameraRunningFailManager(base.Manager):
    resource_class = CameraRunningFail
    
    def list(self):
        return self._list('/admin/camera_running_fail', 'camera_running_fail')