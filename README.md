**Number Classification API**

**Overview**

This is a Flask-based API that classifies numbers based on different mathematical properties. Given a number, the API determines whether it is:

* A prime number

* A perfect number

* An Armstrong number

* Even or odd

* The sum of its digits

* A fun fact about the number (using the Numbers API)

**Features**

**Prime Number Check**: Determines if a number is prime.

**Perfect Number Check**: Checks if a number is a perfect number.

**Armstrong Number Check**: Determines if a number is an Armstrong number.

**Even/Odd Check**: Identifies if a number is even or odd.

**Digit Sum Calculation**: Calculates the sum of the digits of a number.

**Fun Fact Fetching**: Retrieves a fun fact about the number using an external API.

**Installation**

**Clone the repository**:

git clone https://github.com/your-username/number-classification-api.git
cd number-classification-api

**Create and activate a virtual environment (optional but recommended)**:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

**Install the required dependencies**:

pip install -r requirements.txt

**Usage**

**Run the Flask application**:

python app.py

**Access the API endpoint by sending a GET request**:

http://127.0.0.1:5000/api/classify-number?number=28

**API Endpoint**

GET /api/classify-number

**Request Parameters**

number (required): The number to classify.

**Example Request**

curl "http://127.0.0.1:5000/api/classify-number?number=28"

**Example Response**

{
  "number": 28,
  "prime_number": false,
  "perfect_number": true,
  "properties": ["even"],
  "digits_sum": 10,
  "fun_fact": "28 is a perfect number, equal to the sum of its proper divisors."
}

**Dependencies**

**Flask**

**Requests**

To install dependencies manually, run:

pip install flask requests

**Contributing**

Feel free to fork this repository, open issues, or submit pull requests.

**Author**
Babatunde Olumoh
