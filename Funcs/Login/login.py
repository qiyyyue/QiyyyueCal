from flask import Blueprint
from Prop.Properties import parse

login_bp = Blueprint("login_bp", __name__, url_prefix="/login")


def wx_code2session(code):
    props = parse("wx_prop.properties")
    appId = props.get("appId")
    appSecret = props.get("appSecret")

    url = "https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code" % (appId, appSecret, code)

    print(url)

    print(props.get('appId'), props.get('appSecret'))

@login_bp.route("/login", methods=['GET', 'POST'])
def login():
    wx_code2session("")
    return "HW"