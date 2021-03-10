#from tornado.wsgi import WSGIContainer
#from tornado.httpserver import HTTPServer
#from tornado.ioloop import IOLoop
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def test():
    return render_template('index.html')

if __name__ == "__main__":
	app.run()
