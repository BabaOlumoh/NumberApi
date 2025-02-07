from flask import Flask, request, Response
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

# Checking if number is a prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Checking if number is a perfect number
def is_perfect(number):
    return number > 0 and sum(i for i in range(1, number) if number % i == 0) == number

# Checking if number is an Armstrong number
def is_armstrong(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    return sum(d ** power for d in digits) == number

# Sum of the digits in a number
def digit_sum(number):
    return sum(int(d) for d in str(number))

# Fetching a fun fact about the number
def get_fun_fact(number):
    response = requests.get(f"http://numbersapi.com/{number}/math")
    return response.text if response.status_code == 200 else "No fun fact available."

@app.route('/')
def home():
    response_data = json.dumps({"message": "Welcome to the Number Classification API!"})
    return Response(response_data, mimetype="application/json")

@app.route("/api/classify-number", methods=['GET'])
def classify_number():
    number_param = request.args.get('number')

    if not number_param:
        response_data = json.dumps({"number": "alphabet", "error": "true"}, indent=4, sort_keys=False)
        return Response(response_data, status=400, mimetype="application/json")

    try:
        number = int(number_param)
    except ValueError:
        response_data = json.dumps({"number": "alphabet", "error": "true"}, indent=4, sort_keys=False)
        return Response(response_data, status=400, mimetype="application/json")

    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 != 0 else "even")

    response_data = json.dumps({
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }, indent=4, sort_keys=False)

    return Response(response_data, mimetype="application/json")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
