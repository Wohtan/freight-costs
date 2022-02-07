from functions import *
from constants import *

def calculate_costs(input_data):
    ##Performs currency exchange if needed

    if input_data['currency'] != 'MXN':
        input_data['EXW/FCA value'] *= exchange_rates[input_data['currency']]

    weight = calculate_weight(input_data)

    costs = weight_costs_query(weight)

    customs_value = input_data['EXW/FCA value'] + costs['intl freight']

    costs.update(customsval_costs_query(customs_value))

    costs['DTA'] = round(customs_value * 0.008,2)

    costs['IGI'] = round(customs_value * input_data['IGI'],2)

    costs.update(fixed_costs)

    nonfree_surcharge = costs['additional handling'] + costs['keeping'] + costs['storage']

    maneuvers_total = costs['handling'] + costs['maneuvers'] + nonfree_surcharge

    costs['maneuvers total'] = maneuvers_total

    costs['nonfree surcharge'] = nonfree_surcharge

    costs["agent's fee"] = agents_fee(customs_value, costs)

    costs['customs_value'] = customs_value

    costs["Government's pre-validation"] = 278

    costs['TOTAL'] = round(sum(costs.values()) - costs['maneuvers total'] - costs['nonfree surcharge'],2)

    return costs