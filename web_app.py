from flask import Flask, request, url_for,render_template,jsonify
from freight_costs import calculate_costs
from forms import Input_form

app = Flask(__name__)
app.secret_key = 'secr3t k3y'

@app.route('/')
def home():
    form = Input_form()   
    fields = form.fields

    return render_template('calculate.html', form = form, fields = fields)


@app.route('/calculate')
def calculate():
    input_data = request.get_json()['input_data']
    costs = calculate_costs(input_data)
    return costs 

app.run(debug=True)
