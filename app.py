from flask import Flask, render_template
from dotenv import load_dotenv
load_dotenv()
import os
from config import config

env = os.environ.get('ENV')
if env:
    pass
else:
    env = 'development'

# app = Flask(__name__, static_folder='templates', instance_relative_config=True)
app = Flask(__name__, static_folder='static', instance_relative_config=True)

app.config.from_object(config[env])  # from ./config.py


# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

app.config.from_pyfile('config.py')  # from ./instance/config.py
app_config = app.config
# print(app_config)

from model import *

"""Request結束關閉資料庫連接"""
@app.teardown_appcontext
def shutdown_session(exception=None):  # exception=None 很重要
    db_session.remove()


@app.route('/hello')
def hello():
    q_user = User.query.first()
    return 'Hello, {}! {}'.format(q_user.name, app.config['SQLALCHEMY_URL'])


@app.route('/bootstrap_demo')
def demo():
    return render_template('bootstrap_demo.html')


@app.route('/')
def hello_world():
    return render_template('hello-world/dist/index.html')


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0')

