from flask import Flask, request
from freight_costs import calculate_costs

app = Flask(__name__)


@app.route('/calculate')
def freight_costs():
    input_data = request.get_json()['input_data']
    costs = calculate_costs(input_data)
    return costs 

app.run(debug=True)
