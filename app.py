from flask import Flask
from flask import render_template

app = Flask(__name__)


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


app.run(host='0.0.0.0', port=81)
