from flask import Blueprint, request, json


cal_bp = Blueprint("cal_bp", __name__, url_prefix="/calculator")


@cal_bp.route("/", methods=['GET', 'POST'])
def calculator():
    cal_str = request.args.get("cal_str", None)

    cal_res = 0

    return json.dumps({"code": "True", 'msg': '', "cal_res": cal_res}, ensure_ascii=False)