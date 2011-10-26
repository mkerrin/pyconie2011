import webob.dec

import paste.urlmap

@webob.dec.wsgify
def hello(request):
    name = " ".join(request.path_info.split("/"))
    if not name:
        name = "World"
    return webob.Response("Hello, %s!" % name)


@webob.dec.wsgify
def goodbye(request):
    return webob.Response("Goodbye")


app = paste.urlmap.URLMap()
app["/hello"] = hello
app["/goodbye"] = goodbye


if __name__ == "__main__":
    from paste import httpserver
    httpserver.serve(app, "127.0.0.1", 8000)
