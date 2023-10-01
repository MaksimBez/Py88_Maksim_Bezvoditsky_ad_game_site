from django.forms import ValidationError


def code_validate(code):
    available_codes = (
        'g82nvhr92k19',
        '1mczaurwpji5',
        '832hbdirexoa',
        'qpvu63n8z0tk',
        'zaptuvosqlvu'
    )

    if code not in available_codes:
        raise ValidationError('Not available Code')

    return True

"""
    Создать валидацию из базы данных
"""