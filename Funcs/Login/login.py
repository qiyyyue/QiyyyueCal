from flask import Blueprint, request, json
from Prop.Properties import parse
import urllib


login_bp = Blueprint("login_bp", __name__, url_prefix="/login")


def wx_code2session(code):
    props = parse("wx_prop.properties")
    appId = props.get("appId")
    appSecret = props.get("appSecret")
    baseUrl = props.get('url_code2Session')

    url = baseUrl + "?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code" % (appId, appSecret, code)

    data = urllib.request.urlopen(url).read()
    user_info = data.decode('UTF-8')

    return user_info

@login_bp.route("/", methods=['GET', 'POST'])
def login():
    js_code = request.args.get('js_code', None)

    if js_code == None:
        return json.dumps({"code": "False", 'msg': 'no js_code', "user_info": ""}, ensure_ascii=False)

    user_info = wx_code2session(js_code)

    return json.dumps({"code": "True", 'msg': '', "user_info": user_info}, ensure_ascii=False)