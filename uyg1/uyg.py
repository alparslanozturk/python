###
### FLASK_APP=uyg.py FLASK_ENV=development flask run --host=0.0.0.0
###

import time
import redis
from flask import Flask

uyg = Flask(__name__)
kes = redis.Redis(host='redis', port=6379)


def ziyaret():
        return kes.incr('ziyaretler')


@uyg.route("/")
def kok():
        sayac = ziyaret()
        return "Kok dizin {} kez ziyaret edilmiştir.\n".format(sayac)

@uyg.route("/giris")
def giris(): return "<h1> Giris Sayfasi </h1>"
