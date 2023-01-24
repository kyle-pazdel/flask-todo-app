from flask import Flask
from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request
app = Flask(__name__)


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
