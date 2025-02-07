from flask import Flask, request, jsonify
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app)

# Checking if number is a prime
def prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Checking if number is a perfect number
def perfect_number(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number


# Checking if it's an armstrong
def armstrong_number(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    return sum(d ** power for d in digits) == number

# Sum of the number
def digits_sum(number):
    return sum(int(d) for d in str(number))


print(digits_sum(371))

# Fun-fact Api


def get_fun_fact(number):
    response = requests.get(f"http://numbersapi.com/{number}/math")
    return response.text if response.status_code == 200 else "No fun fact available."


@app.route("/api/classify-number", methods=['GET'])
def classify_number():
    number_param = request.args.get('number')

# Error Handling
    try:
        number = int(number_param)
    except (TypeError, ValueError):
        return jsonify({"number": "alphabet", "error": "true"}), 400
    
# Checking for number properties
    number = int(number_param)


    properties = []
    if armstrong_number(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 != 0 else "even")

    json_response = {
        "number": number,
        "prime_number": prime_number(number),
        "perfect_number": perfect_number(number),
        "properties": properties,
        "digits_sum": digits_sum(number),
        "fun_fact": get_fun_fact(number)
    }
    
    return jsonify(json_response)

if __name__ == "__main__":
    app.run(debug=True)
  
    
    