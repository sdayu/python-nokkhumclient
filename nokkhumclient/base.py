'''
Created on Feb 26, 2013

@author: boatkrap
'''

class Manager:
    
    resource_class = None
    def __init__(self, api):
        self.api = api
        
    def _list(self, url, response_key, body=None):
        response = self.api.http_client.get(url)
        data = response[response_key]
        
        return [self.resource_class(self, res) for res in data]
    
    def _get(self, url, response_key):
        response = self.api.http_client.get(url)
        return self.resource_class(self, response[response_key])
        
    def _delete(self, url):
        response = self.api.http_client.delete(url)
    
    def _create(self, url, response_key, body=None):
        response = self.api.http_client.get(url, body)
        return self.resource_class(self, response[response_key])
        
    def _update(self, url, response_key, body=None):
        response = self.api.http_client.get(url, body)
        return self.resource_class(self, response[response_key])
        
        
class Resource:
    def __init__(self, manager, info, loaded=False):
        self.manager = manager
        self._info = info
        self._loaded = loaded
        self._add_details(info)
        
    
    def _add_details(self, info):
        for (k, v) in info.items():
            try:
                setattr(self, k, v)
            except AttributeError:
                # In this case we already defined the attribute on the class
                pass
            
    def __getattr__(self, k):

        # print("get key: ", k)
        if k not in self.__dict__:
            if not self.is_loaded():
                self.get()
                return self.__getattr__(k)

            raise AttributeError(k)
        else:
            return self.__dict__[k]


    def get(self):
        # set_loaded() first ... so if we have to bail, we know we tried.
        self.set_loaded(True)
        if not hasattr(self.manager, 'get'):
            return

        new = self.manager.get(self.id)
        if new:
            # print("new._info:", new._info)
            self._add_details(new._info)

    def is_loaded(self):
        return self._loaded

    def set_loaded(self, val):
        self._loaded = val