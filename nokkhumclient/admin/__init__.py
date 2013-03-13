from . import cameras
from . import command_log
from . import compute_nodes
from . import camera_command_queue
from . import cpu_information
from . import memory_information
from . import camera_operating
from . import users
from . import camera_running_fail


class AdministratorClient:
    def __init__(self, client):
        self.client = client
        
        self.cameras = cameras.CameraManager(self.client)
        self.camera_operating = camera_operating.CameraOperatingManager(self.client)
        self.camera_command_queue = camera_command_queue.CameraCommandQueueManager(self.client)
        self.command_log = command_log.CommandLogManager(self.client)
        self.compute_nodes = compute_nodes.ComputeNodeManager(self.client)
        self.cpu_information = cpu_information.CPUInformationManager(self.client)
        self.memory_information = memory_information.MemoryInformationManager(self.client)
        self.users = users.UserManager(self.client)
        self.camera_running_fail = camera_running_fail.CameraRunningFailManager(self.client)