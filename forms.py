from random import choices
from xml.dom import ValidationErr
from flask_wtf import FlaskForm

from wtforms import (StringField, 
DecimalField, 
SelectField,
SubmitField)

from wtforms.validators import (
    DataRequired,
    NumberRange,
    ValidationError
)

##Custom validators
def check_ammount_en(form,field):
    value = int(form.value.data)
    currency = form.currency.data

    if currency == 'EUR' and value > 70000:
        raise ValidationError('Values over 70K EUR are not allowed')

    elif currency == 'MXN' and value > 1500000:
        raise ValidationError('Values over 1.5 MM MXN are not allowed')

    elif currency == 'USD' and value > 80000:
        raise ValidationError('Values over 80K USD are not allowed')

    elif currency == 'CHF' and value > 73000:
        raise ValidationError('Values over 73K CHF are not allowed')

    else:
        return

def check_ammount_es(form,field):
    value = int(form.value.data)
    currency = form.currency.data

    if currency == 'EUR' and value > 70000:
        raise ValidationError('No se permiten valores sobre 70K EUR')

    elif currency == 'MXN' and value > 1500000:
        raise ValidationError('No se permiten valores sobre 1.5 MM MXN')

    elif currency == 'USD' and value > 80000:
        raise ValidationError('No se permiten valores sobre 80K USD')

    elif currency == 'CHF' and value > 73000:
        raise ValidationError('No se permiten valores sobre 73K CHF')

    else:
        return


class Input_form_en(FlaskForm):
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
            check_ammount_en],
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

    submit = SubmitField('Calculate')  

    fields = ['weight',
    'height',
    'length',
    'depth',
    'value',
    'currency',
    'taxes',]

class Input_form_es(FlaskForm):
    weight = DecimalField(
        'Peso',
            [DataRequired(),
            NumberRange(min=0.05,
            max = 50,
            message = 'Valor fuera de rango'
            )],
        places= 1,
    )

    height = DecimalField(
        'Altura',
            [DataRequired(),
            NumberRange(min=5,
            max = 150,
            message = 'Valor fuera de rango'
            )],
        places= 1,
    )  
    
    length = DecimalField(
        'Ancho',
            [DataRequired(),
            NumberRange(min=5,
            max = 150,
            message = 'Valor fuera de rango'
            )],
        places= 1,
    )

    depth = DecimalField(
        'Largo',
            [DataRequired(),
            NumberRange(min=5,
            max = 150,
            message = 'Valor fuera de rango'
            )],
        places= 1,
    )       

    value = DecimalField(
        'Valor EXW/FCA',
            [DataRequired(),
            check_ammount_es],
        places= 1,
    )     

    currency = SelectField(
        'Moneda',
            [DataRequired()],
        choices=[
            ('EUR'),
            ('CHF'),
            ('MXN'),
            ('USD')
        ]
    )    

    taxes = SelectField(
        'Impuestos',
            [DataRequired()],
        choices=[
            ('5%'),
            ('0%'),
            ('10%'),
            ('15%')
        ]
    )     

    submit = SubmitField('Calcular')  

    fields = ['weight',
    'height',
    'length',
    'depth',
    'value',
    'currency',
    'taxes',]