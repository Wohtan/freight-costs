from functions import *
from constants import *

def calculate_costs(input_data):
    ##Performs currency exchange if needed

    if input_data['currency'] != 'MXN':
        input_data['value'] = float(input_data['value']) * exchange_rates[input_data['currency']]

    weight = float(calculate_weight(input_data))

    costs = weight_costs_query(weight)

    customs_value = float(input_data['value']) + costs['intl freight']

    costs.update(customsval_costs_query(customs_value))

    costs['DTA'] = round(customs_value * 0.008,2)

    costs['IGI'] = round(customs_value * int(input_data['taxes'].replace('%',''))/100,2)

    costs.update(fixed_costs)

    nonfree_surcharge = costs['additional handling'] + costs['keeping'] + costs['storage']

    maneuvers_total = costs['handling'] + costs['maneuvers'] + nonfree_surcharge

    costs['maneuvers total'] = maneuvers_total

    costs['nonfree surcharge'] = nonfree_surcharge

    costs["agent's fee"] = agents_fee(customs_value, costs)

    costs['customs value'] = round(customs_value,2)

    costs["Government's pre-validation"] = 278

    costs['TOTAL'] = round(sum(costs.values())
    - costs['maneuvers total'] 
    - costs['nonfree surcharge']
    - costs['customs value']
    ,0)

    return costs