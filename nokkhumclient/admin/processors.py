'''
Created on Mar 1, 2013

@author: boatkrap
'''

from .. import processors
from . import compute_nodes
class Processor(processors.Processor):
    
    @property
    def compute_node(self):
        if 'compute_node' in self._info:
            return compute_nodes.ComputeNode(self.manager.api.admin.compute_nodes, self._info['compute_node'])
        return None


class ProcessorManager(processors.ProcessorManager):
    resource_class = Processor
    
    def list(self):
        return self._list('/admin/processors', "processors")
    
    def get(self, processor_id):
        return self._get('/admin/processors/%s'%str(processor_id), "processor")
    
    def update(self, processor, action):
        body = dict(
                    processor_operating=dict(action=action)
                    )
        return self._update('/admin/processors/%s'%str(processor.id), "processor", body)