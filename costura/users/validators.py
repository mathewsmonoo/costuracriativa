import re
from django.core import validators
from django.core.exceptions import ValidationError

username_validator = validators.RegexValidator(
    re.compile('^[\w.@+-]+$'),
    'Informe um nome de usuário válido. '
    'Este valor deve conter apenas letras, números '
    'e os caracteres: @/./+/-/_ .', 'invalid'
)

def validate_cpf(value):
    reg_check = re.compile('^\d{3}\.?\d{3}\.?\d{3}\-?\d{2}$')
    if not reg_check.match(value):
        raise ValidationError(
            ('Não é um CPF válido!'),
            params={'value': value},
        )
    clean_value = value
    clean_value = clean_value.replace(".", "")
    clean_value = clean_value.replace("-", "")
    clean_value = [int(i) for i in clean_value]

    if len(clean_value) != 11:
        raise ValidationError(
            ('Não é um cpf válido!'),
            params={'value': value},
        )
        
    all_elem_equal = all(elem == clean_value[0] for elem in clean_value)
    if all_elem_equal:
        raise ValidationError(
            ('Não é um cpf válido!'),
            params={'value': value},
        )
    
    last_two = clean_value[-2:]
    ten_to_two = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    eleven_to_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    # First Digit Verification
    result = 0
    for j in range(9):
        result += clean_value[j] * ten_to_two[j]
    
    first_remainder = (result * 10) % 11
    if first_remainder != last_two[0]:
        raise ValidationError(
            ('Não é um cpf válido!'),
            params={'value': value},
        )
    else:
        # Second Digit Verification
        second_result = 0
        for k in range(10):
            second_result += clean_value[k] * eleven_to_2[k]
        second_remainder = (second_result * 10) % 11
        if second_remainder != last_two[1]:
            raise ValidationError(
                ('Não é um cpf válido!'),
                params={'value': value},
            )
    final_value = []
    final_value.append(str(i) for i in clean_value[:3])
    final_value.append('.')
    final_value.append(str(i) for i in clean_value[3:6])
    final_value.append('.')
    final_value.append(str(i) for i in clean_value[6:9])
    final_value.append('-')
    final_value.append(str(i) for i in last_two)
    print(final_value)
    return final_value