def hello_app(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    return ["Hello, World!"]


if __name__ == "__main__":
    from paste import httpserver
    httpserver.serve(hello_app, "127.0.0.1", 8000)
