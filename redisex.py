import json

import webob.dec

import redis

class data(object):

    def __init__(self, host, key):
        self.r = redis.Redis(host)
        self.k = key

    @webob.dec.wsgify
    def __call__(self, request):
        data = self.r.get(self.k)
        return webob.Response(
            json.dumps(data),
            content_type = "application/json"
            )


if __name__ == "__main__":
    from paste import httpserver
    httpserver.serve(data("localhost", "redisex.key"), "127.0.0.1", 8000)
