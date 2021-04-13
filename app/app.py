from pymemcache.client import base
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
memcache_client = base.Client(("localhost", 11211))


@app.route('/<num>')
def get_fibo_num(num):
    fibo = memcache_client.get(num)
    if fibo is None:
        fibo = count_fibo_num(int(num))        
        memcache_client.set(num, fibo)
    return jsonify(fibo=int(fibo))

def count_fibo_num(num):
    fibo, fibo_next = 0, 1
    for _ in range(num - 1):
        fibo, fibo_next = fibo_next, fibo + fibo_next
    return fibo
