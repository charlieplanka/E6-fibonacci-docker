from pymemcache.client import base
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
client = base.Client(("localhost", 11211))


@app.route('/')
def get_fibo_num():
    num = int(request.args.get("k"))
    if not num:
        resp = jsonify(success=True)
        resp.status_code = 200
        return resp
    
    fibo = client.get(str(num))
    if fibo is None:
        fibo, fibo_next = 0, 1
        for _ in range(num-1):
            fibo, fibo_next = fibo_next, fibo + fibo_next
        client.set(str(num), fibo)
    
    return jsonify(fibo=int(fibo))
