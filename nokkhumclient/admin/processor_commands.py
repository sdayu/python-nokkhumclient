'''
Created on Mar 6, 2013

@author: boatkrap
'''
from .. import processor_commands
from . import users
from . import processors

class ProcessorCommand(processor_commands.ProcessorCommand):
    @property
    def processor(self):
        return processors.Processor(self.manager.api.admin.processors, self._info['processor'])
    
    @property
    def owner(self):
        return users.User(self.manager.api.admin.users, self._info['owner'])

class ProcessorCommandManager(processor_commands.ProcessorCommandManager):
    resource_class = ProcessorCommand
    
    def list(self):
        return self._list('/admin/processor_commands', 'processor_commands')
    
    def get(self, processor_command_id):
        return self._get('/admin/processor_commands/%s'%str(processor_command_id), 'processor_command')