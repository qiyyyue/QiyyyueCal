import os

from flask import Blueprint, request, json


reward_bp = Blueprint("reward_bp", __name__, url_prefix="/reward")


@reward_bp.route("/", methods=['GET', 'POST'])
def reward():
    openId = request.args.get("openId", None)
    money = request.args.get("money", None)

    try:
        with open("Data/record.txt", 'a') as append:
            append.write(str(openId) + "\t" + str(money) + "\n")
            append.flush()
            append.close()
    except Exception as e:
        return json.dumps({"code": "False", 'msg': 'write error'}, ensure_ascii=False)

    return json.dumps({"code": "True", 'msg': ''}, ensure_ascii=False)