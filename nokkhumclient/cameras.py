from . import base
from . import camera_manufactory
from . import camera_model
import datetime

class Camera(base.Resource):

    @property
    def operating(self):
        return self.manager.api.camera_operating.get(self.id)
    
    @property
    def storage(self):
        return self.manager.api.storage.list_by_camera(self.id)
    
    @property
    def camera_model(self):
        return camera_model.CameraModel(
                    self.manager.api.camera_models,
                    self._info['model']
                    )
        
    @camera_model.setter
    def camera_model(self, model):
        if 'model' not in self._info:
            self._info['model'] = {}
        
        self._info['model']['id'] = model.id
        del self._info['model']['manufactory']

class CameraManager(base.Manager):
    resource_class = Camera
    
    def list_cameras_by_project(self, project_id):
        return self._list('/projects/%s/cameras'%str(project_id), 'cameras')
    
    def list(self):
        return self._list('/cameras', "cameras")
    
    def get(self, camera_id):
        return self._get('/cameras/%s'%str(camera_id), "camera")
    
    def get_camera_by_project(self, camera_id, project_id):
        return self._get('/projects/%s/cameras/%s'%(str(project_id), str(camera_id)), 'camera')
    
    def delete(self, camera):
        return self._delete('/cameras/%d'%camera.id)
    
    def create(self):
        pass
    
    def update(self, camera):
        for (k,v) in camera._info.items():
            
            try:
                val = getattr(camera, k)
                if v != val:
                    if type(val) is datetime.datetime:
                        val = val.isoformat()
                    camera._info[k] = val
                         
            except:
#                print("key error:", k)
                pass
                
        body = dict(
                camera=camera._info
                )

        return self._update('/cameras/%d'%camera.id, "camera", body)