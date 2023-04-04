import requests


class PretalxAPI():
    def __init__(self, endpoint ,pretalx_token=""):
        self.endpoint = endpoint
        self.pretalx_token = pretalx_token
        self.default_headers = {
            'Accept': 'application/json',
            "Content-Type": 'application/json',
            "Authorization": "Token %s" % (pretalx_token)
        }
    
    def post_reqeust(self, url, headers={}, data={}):
        # python > 3.5
        headers = { **headers, **self.default_headers }
        return requests.request("POST", "%s%s" % (self.endpoint, url), headers=headers, data=data).json()
    
    def get_reqeust(self, url, headers={}, query_params={}):
        headers = { **headers, **self.default_headers }
        return requests.request("GET", "%s%s" % (self.endpoint, url), headers=headers).json()
    