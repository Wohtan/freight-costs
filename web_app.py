from flask import Flask, redirect, request, url_for,render_template,jsonify
from freight_costs import calculate_costs
from forms import Input_form

app = Flask(__name__)
app.secret_key = 'secr3t k3y'

@app.route('/',methods=["POST",'GET'])
def home():
    form = Input_form()   
    fields = form.fields
    input_data = request.form.to_dict()

    if form.validate_on_submit(): 
        costs = calculate_costs(input_data)      
        return render_template('calculate.html', form = form, fields = fields, costs=costs)

    return render_template('calculate.html', form = form, fields = fields, costs = [])


app.run(debug=True)
