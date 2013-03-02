from . import base

class Camera(base.Resource):

    @property
    def operating(self):
        return self.manager.api.camera_operating.get(self.id)
    
    @property
    def storage(self):
        return self.manager.api.storage.list_by_camera(self.id)

class CameraManager(base.Manager):
    resource_class = Camera
    
    def list_cameras_by_projects(self, project_id):
        return self._list('/projects/%s/cameras'%str(project_id), 'cameras')
    
    def list(self):
        return self._list('/cameras', "cameras")
    
    def get(self, camera_id):
        return self._get('/cameras/%s'%str(camera_id), "camera")
    
    def delete(self, camera):
        return self._delete('/cameras/%d'%camera.id)
    
    def create(self):
        pass
    
    def update(self):
        pass