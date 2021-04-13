from pymemcache.client import base
from flask import Flask
from flask import request
from flask import jsonify
import os

app = Flask(__name__)
memcache_client = base.Client(("localhost", 11211))
# port = int(os.environ.get("PORT", 5000))


@app.route('/<num>')
def get_fibo_num(num):
    fibo = memcache_client.get(num)
    if fibo is None:
        fibo = count_fibo_num(int(num))        
        memcache_client.set(num, fibo)
    return jsonify(fibo=int(fibo)), 200

def count_fibo_num(num):
    fibo, fibo_next = 0, 1
    for _ in range(num - 1):
        fibo, fibo_next = fibo_next, fibo + fibo_next
    return fibo


# if __name__ == '__main__':
#     app.run(debug=True, host='127.0.0.1', port=port)
