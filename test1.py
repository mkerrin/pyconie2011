import webtest

import routeex

app = webtest.TestApp(routeex.app)
res = app.get("/", expect_errors = True)
assert res.status_int == 404

res = app.get("/hello")
assert res.headers["Content-Type"].startswith("text/html")
assert res.body == "Hello, World!"

res = app.get("/hello/Michael/Kerrin")
assert res.headers["Content-Type"].startswith("text/html")
assert res.body == "Hello,  Michael Kerrin!"
