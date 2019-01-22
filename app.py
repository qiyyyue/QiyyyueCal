import flask
from flask import Flask
from Funcs.Login.login import login_bp
from Funcs.Calculator.Calculator import cal_bp
from Funcs.Reward.Reward import reward_bp


app = Flask(__name__)


app.register_blueprint(login_bp)
app.register_blueprint(cal_bp)
app.register_blueprint(reward_bp)

if __name__ == '__main__':
    app.run()