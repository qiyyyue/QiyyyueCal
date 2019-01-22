import flask
from flask import Flask
from Funcs.Login.login import login_bp


app = Flask(__name__)


app.register_blueprint(login_bp)

if __name__ == '__main__':
    app.run()