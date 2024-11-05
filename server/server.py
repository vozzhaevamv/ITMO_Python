from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():

    a = request.args.get('a')
    b = request.args.get('b')
    a = float(a)
    b = float(b)
    result = a + b

    message = f"Сложение чисел: {a} + {b} = {result}"
    return jsonify({
        "message": message,
        "a": a,
        "b": b,
        "result": result
    })

if __name__ == '__main__':
    app.run(debug=True)