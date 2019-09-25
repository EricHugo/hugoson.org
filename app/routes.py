from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "There seems to be nothing here."
#http_server = HTTPServer(WSGIContainer(app))
#http_server.listen(int(5000),address="198.54.116.15")
#IOLoop.instance().start()

if __name__ == "__main__":
	app.run()
