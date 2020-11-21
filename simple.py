from flask import Flask, request, jsonify
from multiprocessing import Value

counter = Value('i', 0)
app = Flask(__name__)

@app.route('/')
def index():
    with counter.get_lock():
        counter.value += 1
        out = counter.value
    return jsonify({'total': out, 'client': request.remote_addr})

app.run(host='0.0.0.0', processes=1)
