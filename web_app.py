from flask import Flask, request,render_template
from freight_costs import calculate_costs
from functions import check_language

app = Flask(__name__)
app.secret_key = 'secr3t k3y'

if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.run()

@app.route('/',methods=["POST",'GET'])
def home():
    language, form = check_language()

    fields = form.fields
    input_data = request.form.to_dict()

    if form.validate_on_submit(): 
        costs = calculate_costs(input_data)    
        return render_template(f'calculate_{language}.html', form = form, fields = fields, costs=costs)

    return render_template(f'calculate_{language}.html', form = form, fields = fields, costs = [])

