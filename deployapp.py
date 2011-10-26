import webob.dec

class Hello(object):

    def __init__(self, local_conf, name = "", **global_conf):
        self.name = name

    @webob.dec.wsgify
    def __call__(self, request):
        return webob.Response("Hello, %s!" % self.name)
