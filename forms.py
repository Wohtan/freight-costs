from random import choices
from flask_wtf import FlaskForm

from wtforms import (StringField, 
DecimalField, 
SelectField,
SubmitField)

from wtforms.validators import (
    DataRequired,
    NumberRange,
)

class Input_form(FlaskForm):
    weight = DecimalField(
        'Weight',
            [DataRequired(),
            NumberRange(min=0.05,
            max = 50,
            message = 'Value out of range'
            )],
        places= 1,
    )

    height = DecimalField(
        'Height',
            [DataRequired(),
            NumberRange(min=5,
            max = 150,
            message = 'Value out of range'
            )],
        places= 1,
    )  
    
    length = DecimalField(
        'Length',
            [DataRequired(),
            NumberRange(min=5,
            max = 150,
            message = 'Value out of range'
            )],
        places= 1,
    )

    depth = DecimalField(
        'Depth',
            [DataRequired(),
            NumberRange(min=5,
            max = 150,
            message = 'Value out of range'
            )],
        places= 1,
    )       

    value = DecimalField(
        'EXW/FCA value',
            [DataRequired(),
            NumberRange(min=1,
            max = 500000,
            message = 'Value out of range'
            )],
        places= 1,
    )     

    currency = SelectField(
        'Currency',
            [DataRequired()],
        choices=[
            ('EUR'),
            ('CHF'),
            ('MXN'),
            ('USD')
        ]
    )    

    taxes = SelectField(
        'Tax rate',
            [DataRequired()],
        choices=[
            ('5%'),
            ('0%'),
            ('10%'),
            ('15%')
        ]
    )     

    submit = SubmitField('Submit')  

    fields = ['weight',
    'height',
    'length',
    'depth',
    'value',
    'currency',
    'taxes',]