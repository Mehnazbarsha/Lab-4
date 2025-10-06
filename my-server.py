from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
   return " you called \n"

@app.route("/echo", methods=['POST'])
def echo():
   return "You said: " + request.form['text']

def trial_division(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2
    if n > 1:
        factors.append(n)
    return factors

@app.route("/factor", methods=['GET', 'POST'])
def factor():
    try:
        if request.method == 'GET':
            inINT = request.args.get('number', type=int)
        else:  
            inINT = request.form.get('number', type=int)
        
        if inINT is None:
            return jsonify({"error": "Missing 'number' parameter"}), 400
        
        if inINT < 1:
            return jsonify({"error": "Number must be positive"}), 400
        
        if inINT == 1:
            factors = [1]
        else:
            factors = [1] + trial_division(inINT)
        
        return jsonify({"number": inINT, "factors": factors}), 200
    
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid number format"}), 400

if __name__ == "__main__":
   app.run(host='0.0.0.0')