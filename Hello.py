from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
   return '<a href="hi2/">Hello World2</a>'



@app.route('/hello/<name>')
def hello_world2(name):
   addString = "hi2"
   return '<a href="/hello/' + addString +name+ '">Hello %s</a>' %name


@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Welcome %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))


if __name__ == '__main__':
   app.debug = True
   app.run()