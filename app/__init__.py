from flask import Flask

from Resumeproject.config import Config

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
app.use_static_for = True
from Resumeproject.app import routes
