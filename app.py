from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    title = 'Sample title'
    users = ['Kyle', 'Nelson', 'Greg']
    return render_template('index.html', title=title, members=users)


app.run(host='0.0.0.0', port=81)
