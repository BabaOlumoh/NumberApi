from flask import Flask, request, Response
from flask_cors import CORS
import requests
import json
import os

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
    if number == 0:
        return False
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number


# Checking if it's an armstrong
def armstrong_number(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    return sum(d ** power for d in digits) == number

# Sum of the number
def digit_sum(number):
    return sum(int(d) for d in str(number))


def get_fun_fact(number):
    response = requests.get(f"http://numbersapi.com/{number}/math")
    return response.text if response.status_code == 200 else "No fun fact available."

@app.route('/')
def home():
    return Response(json.dumps({"message": "Welcome to the Number Classification API!"}, indent=4),
                    status=200, content_type="application/json")

@app.route("/api/classify-number", methods=['GET'])
def classify_number():
    number_param = request.args.get('number')

# Error Handling
    try:
        number = int(number_param)
    except (TypeError, ValueError):
                return Response(json.dumps(json_response, indent=4), status=400, content_type="application/json")

    
# Checking for number properties
    number = int(number_param)


    properties = []
    if armstrong_number(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 != 0 else "even")

    json_response = {
        "number": number,
        "is_prime": bool(is_prime(number)),
        "is_perfect": bool(is_perfect(number)),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }
    
    return Response(json.dumps(json_response, indent=4), status=200, content_type="application/json")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
  
    
