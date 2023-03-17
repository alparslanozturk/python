from: python:3.9-apline
workdir /test
env FLASK_APP=uyg.py
env FLASK_ENV=development
env FLASK_RUN_HOST=0.0.0.0
run apk add --no-cache build-base musl-dev linux-headers
copy requirements.txt requirements.txt
run pip install -r requirements.txt
expose 5000
copy . .
cmd ["flask", "run"]
