from django.forms import ValidationError


def promocode_validate(promocode):
    available_promocodes = (
        'g82nvhr92k19',
        '1mczaurwpji5',
        '832hbdirexoa',
        'qpvu63n8z0tk',
        'zaptuvosqlvu',
        'vpr28f7a1mc7',
        'bfjs49fltpf1',
        'mcjj371bfp4e',
        'x892jfu21smd',
        'abyrnf83zyr7',
        'hjnfv489idsj'
    )

    if promocode not in available_promocodes:
        raise ValidationError('Not available promocode')

    return True

"""
    Создать валидацию из базы данных
"""