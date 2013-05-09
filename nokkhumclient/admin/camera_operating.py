'''
Created on Mar 1, 2013

@author: boatkrap
'''

from .. import camera_operating
from . import compute_nodes
class CameraOperating(camera_operating.CameraOperating):
    
    @property
    def compute_node(self):
        if 'compute_node' in self._info:
            return compute_nodes.ComputeNode(self.manager.api.admin.compute_nodes, self._info['compute_node'])
        return None


class CameraOperatingManager(camera_operating.CameraOperatingManager):
    resource_class = CameraOperating
    
    def get(self, camera_id):
        return self._get('/admin/cameras/%s/operating'%str(camera_id), "camera_operating")
    
    def update(self, camera, action):
        body = dict(
                    camera_operating=dict(action=action)
                    )
        return self._update('/admin/cameras/%s/operating'%str(camera.id), "camera_operating", body)