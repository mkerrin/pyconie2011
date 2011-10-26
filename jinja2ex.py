import webob.dec

import jinja2

env = jinja2.Environment(loader = jinja2.FileSystemLoader("."))
tmpl = env.get_template("hello.jinja2")

class home(object):

    def __init__(self, default_name):
        self.default_name = default_name

    @webob.dec.wsgify
    def __call__(self, request):
        return webob.Response(
            tmpl.render(name = request.params.get("name", self.default_name))
            )


if __name__ == "__main__":
    from paste import httpserver
    httpserver.serve(home("Michael"), "127.0.0.1", 8000)
