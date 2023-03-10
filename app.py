from flask import Flask
from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request, make_response
app = Flask(__name__)

# Sample to demonstrate cookie storage and passing


@app.route('/cookieform')
def cookie_form():
    return render_template('cookieform.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']

        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)

        return resp


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>Cookie data: ' + name + '</h1>'

# Smaple to demonstrate data submission via POST from one template to another


@app.route('/student')
def student():
    return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)


# Sample to show connectivity between route, html template, and static file (in this case JS file with a function)


@app.route("/say-hello")
def say_hello():
    return render_template("say-hello.html")

# Sample redirect from login to dashboard


@app.route('/dashboard/<name>')
def dashboard(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('dashboard', _external=True, name=user))
    else:
        user = request.args.get('name')
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=81)


# Sample index route
@app.route('/')
@app.route('/index')
def index():
    title = 'Sample title'
    users = ['Kyle', 'Nelson', 'Greg']
    return render_template('index.html', title=title, members=users)


# Sample route
@app.route('/hello')
def hello_world():
    return "hello world"


# Sample route with param
post = {"id": 1, "1": "Post 1", "body": "The body text of Post 1"}


@app.route('/posts/<id>')
def show_post(id=0):
    return f"Title: {post[str(id)]}"

# Sample route with multiple params


@app.route('/create/<first_name>/<last_name>')
def create(first_name=None, last_name=None):
    return 'Hello ' + first_name + ', ' + last_name

# app.run(host='0.0.0.0', port=81)
