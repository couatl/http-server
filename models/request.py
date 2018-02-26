
class Request(object):
    def __init__(self, method, url,
                 headers={}, params={}):

        self.method = method
        self.url = url
        self.headers = headers
        self.params = params
