import json

import requests


class BaseClient:
    
    def __init__(self, base_url):
        self.base_url = base_url

    def get_request(self, path_url, headers, params=None, data=None):
        print('base url', self.base_url)
        print(path_url)
        print(headers)
        print(params)
        if params:
            return requests.get(self.base_url + path_url, headers=headers, params=params, data=data)
        return requests.get(self.base_url + path_url, headers=headers, data=data)

    def post_request(self, path_url, data, headers):
        return requests.post(self.base_url + path_url, data=data, headers=headers)
    
    def put_request(self, path_url, headers, data=None):
        return requests.put(self.base_url + path_url, headers=headers, data=data)
    
    def delete_request(self, path_url, headers, data=None):
        if data is not None:
            return requests.delete(self.base_url + path_url, data=json.dumps(data), headers=headers)
        return requests.delete(self.base_url + path_url, headers=headers)
