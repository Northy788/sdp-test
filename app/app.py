from flask import Flask, jsonify
from math import isqrt
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Welcome to Flask api', 200
@app.route('/is_prime/<x>')
def is_prime(x):
    try:
        x = int(x)
        if x == 2 or x == 3: 
            return 'true', 200
        if x <= 1 or x % 2 == 0 or x % 3 == 0:
            return 'false', 200
        stop = isqrt(x)
        for i in range(5, stop + 1, 6):
            if x % i == 0 or x % (i + 2) == 0:
                return 'false', 200
    except ValueError:
        return 'Invalid input', 400
    return 'true', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)