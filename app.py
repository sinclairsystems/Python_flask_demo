from flask import Flask, jsonify, request
import PAYE
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Shafquat!'


@app.route('/getNetIncome/', methods=['POST'])
def netIncome():
    gross_income = request.get_json()
    print(gross_income)
    gross = float(gross_income["gross_income"])
    return jsonify(gross - PAYE.totalTax(gross))


if __name__ == '__main__':
    app.run()





