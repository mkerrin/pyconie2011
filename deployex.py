import paste.deploy
from paste import httpserver

app = paste.deploy.loadapp("config:deploy.ini")
httpserver.serve(app, "127.0.0.1", 8000)
