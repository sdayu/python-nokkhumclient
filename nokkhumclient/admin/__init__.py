from . import cameras
from . import compute_nodes
from . import processor_command_queue
from . import processor_commands
from . import processors
from . import cpu_information
from . import memory_information
from . import disk_information
from . import processor_operating
from . import users
from . import processor_running_fail
from . import cache


class AdministratorClient:
    def __init__(self, client):
        self.client = client
        
        self.cameras = cameras.CameraManager(self.client)
        self.processors = processors.ProcessorManager(self.client)
        self.processor_operating = processor_operating.ProcessorOperatingManager(self.client)
        self.processor_command_queue = processor_command_queue.ProcessorCommandQueueManager(self.client)
        self.processor_commands = processor_commands.ProcessorCommandManager(self.client)
        self.compute_nodes = compute_nodes.ComputeNodeManager(self.client)
        self.cpu_information = cpu_information.CPUInformationManager(self.client)
        self.memory_information = memory_information.MemoryInformationManager(self.client)
        self.disk_information = disk_information.DiskInformationManager(self.client)
        self.users = users.UserManager(self.client)
        self.processor_running_fail = processor_running_fail.ProcessorRunningFailManager(self.client)
        
        self.cache = cache.CacheManager(self.client)