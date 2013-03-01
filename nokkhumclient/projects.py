'''
Created on Feb 27, 2013

@author: boatkrap
'''

from . import base

class Project(base.Resource):
    
    @property
    def cameras(self):

        return self.manager.api.cameras.list_cameras_by_projects(self.id)
    

class ProjectManager(base.Manager):
    resource_class = Project
    
    def list_user_projects(self, user_id):
        return self._list('/users/%d/projects'%user_id, "projects")
    
    def list(self):
        return self._list('/projects', "projects")
    
    def get(self, project_id):
        return self._get('/projects/%s'%str(project_id), "project")
    
    def delete(self, project):
        return self._delete('/projects/%d'%project.id)
    
    def create(self):
        pass
    
    def update(self):
        pass