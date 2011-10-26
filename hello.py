import webob.dec

@webob.dec.wsgify
def hello(request):
    return webob.Response("Hello, World!")


if __name__ == "__main__":
    from paste import httpserver
    httpserver.serve(hello, "127.0.0.1", 8000)

