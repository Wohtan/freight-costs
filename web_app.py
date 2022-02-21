from ssl import SSLSession
from flask import Flask, redirect, request, url_for,render_template,jsonify, session
from freight_costs import calculate_costs
from forms import Input_form_en, Input_form_es

app = Flask(__name__)
app.secret_key = 'secr3t k3y'

@app.route('/',methods=["POST",'GET'])
def home():
    language = request.args.get('lang')
    
    if not language:
        language = 'es'

    if language == 'es':        
        form = Input_form_es()   
    else:
        form = Input_form_en()

    fields = form.fields
    input_data = request.form.to_dict()

    if form.validate_on_submit(): 
        costs = calculate_costs(input_data)      
        return render_template(f'calculate_{language}.html', form = form, fields = fields, costs=costs)

    return render_template(f'calculate_{language}.html', form = form, fields = fields, costs = [])

app.run(debug=True)
