import webob.dec
import paste.urlmap
import paste.reloader
import jinja2

env = jinja2.Environment(loader = jinja2.FileSystemLoader("."))
whoami = env.get_template("whoami.html")
# paste.reloader.watch_file("whoami.html")

@webob.dec.wsgify
def hi(request):
    if request.method == "POST":
        return webob.Response("Hi, %s" % request.params.get("name"))

    return home(request)


@webob.dec.wsgify
def home(request):
    return webob.Response(whoami.render())


class Router(object):

    def __init__(self, *args, **kw):
        self.app = paste.urlmap.URLMap()
        self.app["/hi"] = hi
        self.app["/"] = home

    def __call__(self, environ, start_response):
        return self.app(environ, start_response)


if __name__ == "__main__":
    from paste import httpserver
    httpserver.serve(app, "127.0.0.1", 8000)
