import re
from django.core import validators
from django.core.exceptions import ValidationError

username_validator = validators.RegexValidator(
    re.compile('^[\w.@+-]+$'),
    'Informe um nome de usuário válido. '
    'Este valor deve conter apenas letras, números '
    'e os caracteres: @/./+/-/_ .', 'invalid'
)

def validate_cpf(cpf):
    reg_check = re.compile('^\d{3}\.?\d{3}\.?\d{3}\-?\d{2}$')
    if not reg_check.match(cpf):
        raise ValidationError(
            ('Não é um CPF válido!'),
            params={'cpf': cpf},
        )
    clean_cpf = cpf
    clean_cpf = clean_cpf.replace(".", "")
    clean_cpf = clean_cpf.replace("-", "")
    clean_cpf = [int(i) for i in clean_cpf]

    if len(clean_cpf) != 11:
        raise ValidationError(
            ('Não é um CPF válido!'),
            params={'cpf': cpf},
        )
        
    all_elem_equal = all(elem == clean_cpf[0] for elem in clean_cpf)
    if all_elem_equal:
        raise ValidationError(
            ('Não é um CPF válido!'),
            params={'cpf': cpf},
        )
    
    last_two = clean_cpf[-2:]
    ten_to_two = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    eleven_to_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    # First Digit Verification
    result = 0
    for j in range(9):
        result += clean_cpf[j] * ten_to_two[j]
    
    first_remainder = (result * 10) % 11
    if first_remainder != last_two[0]:
        raise ValidationError(
            ('Não é um CPF válido!'),
            params={'cpf': cpf},
        )
    else:
        # Second Digit Verification
        second_result = 0
        for k in range(10):
            second_result += clean_cpf[k] * eleven_to_2[k]
        second_remainder = (second_result * 10) % 11
        if second_remainder != last_two[1]:
            raise ValidationError(
                ('Não é um CPF válido!'),
                params={'cpf': cpf},
            )
    final_cpf = []
    final_cpf.append(str(i) for i in clean_cpf[:3])
    final_cpf.append('.')
    final_cpf.append(str(i) for i in clean_cpf[3:6])
    final_cpf.append('.')
    final_cpf.append(str(i) for i in clean_cpf[6:9])
    final_cpf.append('-')
    final_cpf.append(str(i) for i in last_two)
    print(final_cpf)
    return final_cpf