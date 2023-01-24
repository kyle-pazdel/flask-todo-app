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


# posts = [{"id": 1, "1": "Post 1", "body": "The body text of Post 1"},
#          {"id": 2, "2": "Post 2", "body": "The body text of Post 2"},
#          {"id": 3, "3": "Post 3", "body": "The body text of Post 3"}]
post = {"id": 1, "1": "Post 1", "body": "The body text of Post 1"}


@app.route('/posts/<id>')
def show_post(id):
    return f"Title: {post[str(id)]}"


app.run(host='0.0.0.0', port=81)
