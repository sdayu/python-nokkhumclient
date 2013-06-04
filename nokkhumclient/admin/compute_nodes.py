'''
Created on Mar 6, 2013

@author: boatkrap
'''
from .. import base
from . import cpu_information
from . import memory_information
from . import disk_information

class ComputeNode(base.Resource):
    
    @property
    def cpu(self):
        if 'cpu' not in self._info:
            self.get()
        return cpu_information.CPUInformation(self.manager.api.admin.cpu_information, self._info['cpu'])
    
    @property
    def memory(self):
        if 'memory' not in self._info:
            self.get()
        return memory_information.MemoryInformation(self.manager.api.admin.memory_information, self._info['memory'])
    
    @property
    def disk(self):
        if 'disk' not in self._info:
            self.get()
        return disk_information.DiskInformation(self.manager.api.admin.disk_information, self._info['disk'])
    

class ComputeNodeManager(base.Manager):
    resource_class = ComputeNode
    
    def list(self):
        return self._list('/admin/compute_nodes', 'compute_nodes')
    
    def get(self, compute_node_id):
        return self._get('/admin/compute_nodes/%s'%str(compute_node_id), 'compute_node')