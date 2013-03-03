'''
Created on Dec 5, 2012

@author: superizer
'''
import requests
import json

from . import accounts
from . import cameras
from . import camera_operating
from . import projects
from . import storage


class HTTPClient:
    def __init__(self, username, password, host, port=80, secure_connection=False, token=None):
        
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.secure_connection = secure_connection
        self.auth_token = token
        self.user_id = None
        
        self.scheme = "http"
        if self.secure_connection:
            self.scheme = "https"
        
        self.api_url = '%s://%s:%d' %(self.scheme, self.host, self.port)

    def authenticate(self):
        body = {'password_credentials': {'password': self.password, 'username': self.username}}

        response = self.request(self.api_url + '/authentication/tokens', 
                                "POST", 
                                body=body, 
                                headers={})
        if response:
            self.auth_token = response['access']['token']['id']
            self.user_id = response['access']['user']['id']
            return response
        return None
    
    def request(self, url, method, **kwargs):
        kwargs['headers']['Content-Type'] = 'application/json'

        if 'body' in kwargs:
            kwargs['data'] = json.dumps(kwargs['body'])
            del kwargs['body']
            
        response = requests.request(method, 
                                    url,
                                    **kwargs)
        
        if response.status_code == 200:
#            print("response:", response.json())
            return response.json()
        return None
    
    def _cs_request(self, url, method, **kwargs):
        kwargs.setdefault('headers', {})['X-Auth-Token'] = self.auth_token
        
        return self.request(self.api_url + url, 
                            method, 
                            **kwargs)
    
    def get(self, url, **kwargs):
        return self._cs_request(url, 'GET', **kwargs)

    def post(self, url, **kwargs):
        return self._cs_request(url, 'POST', **kwargs)

    def put(self, url, **kwargs):
        return self._cs_request(url, 'PUT', **kwargs)

    def delete(self, url, **kwargs):
        return self._cs_request(url, 'DELETE', **kwargs)
    
    
class Client:
    def __init__(self,
                    username,
                    password, 
                    host="127.0.0.1", 
                    port=80, 
                    secure_connection=False, 
                    token=None):
        
        self.username=username
        self.password=password
        self.host = host
        self.port = port
        self.secure_connection = secure_connection
        
        self.http_client = HTTPClient(username,
                                      password, 
                                      host, 
                                      port, 
                                      secure_connection, 
                                      token
                                      )
        

        self.accounts = accounts.AccountManager(self)
        self.cameras = cameras.CameraManager(self)
        self.camera_operating = camera_operating.CameraOperatingManager(self)
        self.projects = projects.ProjectManager(self)
        self.storage = storage.StorageManager(self)
        
        
    def authenticate(self):
        return self.http_client.authenticate()
