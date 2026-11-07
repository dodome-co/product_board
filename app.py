import random

from flask import Flask

omikujis = ["大吉", "中吉", "小吉", "吉", "凶"]

app = Flask(__name__)


@app.route("/")
def index():
    return "<h2>スパルタキャンプ掲示板</h2><p>宿題忘れないで！</p>"


# control sできれいになおす。

@app.route("/hello/<name>")
def hello(name):
    return f"<p>こんにちは{name}</p>"


@app.route("/omikuji")
def omikuji():#()に入れるとエラーになる
    #omikujis = ["大吉", "中吉", "小吉", "吉", "凶"] この中でしか使わない場合はOK。必要があるところに書く方が好まれる
    unsei = random.choice(omikujis)
    return f"<p>あなたの運勢は{unsei}です</p>"
