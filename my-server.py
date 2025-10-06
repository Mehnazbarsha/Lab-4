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
        # Handle both GET and POST requests
        if request.method == 'GET':
            num_str = request.args.get('number')
        else:  # POST
            num_str = request.form.get('number')
        
        if num_str is None:
            return jsonify({"error": "Missing 'number' parameter"}), 400
        
        try:
            inINT = int(num_str)
        except (ValueError, TypeError):
            return jsonify({"error": "Invalid number format"}), 400
        
        if inINT < 1:
            return jsonify({"error": "Number must be positive"}), 400
        
        # Get factors
        if inINT == 1:
            factors = [1]
        else:
            factors = [1] + trial_division(inINT)
        
        return jsonify(factors), 200
    
    except Exception as e:
        return jsonify({"error": "An error occurred"}), 500

if __name__ == "__main__":
   app.run(host='0.0.0.0')