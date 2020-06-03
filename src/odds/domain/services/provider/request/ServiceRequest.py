import urllib3
import json

class ServiceRequest:

    def __init__(self):
        self.http = urllib3.PoolManager()

    def call(self, url):
        response = self.http.request('GET', url,)
        return json.loads(response.data.decode('utf-8'))



