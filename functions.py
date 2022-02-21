import pandas as pd
from constants import *

def create_tables():
    weight_dependent = [
    "handling",
    "intl freight"]

    weight_tables = {}

    for i in weight_dependent:
        weight_tables[i] = pd.read_csv(f'./CSVs/{i}.csv', dtype = {'weight':'float64'})


    customs_value_dependent = ["complementary services",
    "keeping"
    ]

    customs_value_tables = {}

    for i in customs_value_dependent:
        customs_value_tables[i] = pd.read_csv(f'./CSVs/{i}.csv', dtype = {'customs value':'float64'})
    
    return weight_tables,customs_value_tables

def calculate_weight(input_data):
    height =float(input_data['height'])
    length =float(input_data['length'])
    depth = float(input_data['depth'])
    
    input_weight = float(input_data['weight'])
    vol_weight = (height * length * depth)/5000

    if input_weight > vol_weight:
        return input_weight
    else:
        return vol_weight

def weight_costs_query(weight):
    weight_tables,_ = create_tables()
    query_df = pd.DataFrame()
    query_df['weight'] = [weight]

    for table in weight_tables:
        query_df[table] = pd.merge_asof(query_df['weight'],
        weight_tables[table],
        on= 'weight',
        direction = 'forward').iloc[:,1] ##Appends only the second column

    query_df = query_df.to_dict(orient='records') ## It comes as a list of dictionaries
    query_df = query_df[0] ##Gets rid of the list
    query_df.pop('weight')

    ##The intl. freight is in USD, exchange required:
    query_df['intl freight'] *= exchange_rates['USD']
    query_df['intl freight'] = round(query_df['intl freight'],2)
    return query_df

def customsval_costs_query(customs_value):
    _,customs_value_tables = create_tables()
    query_df = pd.DataFrame()
    query_df['customs value'] = [customs_value]

    for table in customs_value_tables:
        query_df[table] = pd.merge_asof(query_df['customs value'],
        customs_value_tables[table],
        on= 'customs value',
        direction = 'forward').iloc[:,1] ##Appends only the second column

    query_df = query_df.to_dict(orient='records') ## It comes as a list of dictionaries
    query_df = query_df[0] ##Gets rid of the list
    query_df.pop('customs value')

    return query_df   

def agents_fee(customs_value,costs):
    values = [customs_value,
    costs['DTA'],
    costs['IGI'],
    278,
    costs['maneuvers total'],
    costs['nonfree surcharge'],
    costs['DHL management surcharge']]
    values_sum = round(sum(values) * 1.16 * 0.004,2)

    if values_sum > 1000:
        return values_sum
    else:
        return 1000