from django import template

register = template.Library()

@register.filter
def currency_format(value):
    if value < 0:
        return "$ {:,.0f} )".format(value).replace('.', ',').replace(',', '.').replace('-', '( ')
    else:
        return "$ {:,.0f}".format(value).replace('.', ',').replace(',', '.')


@register.filter
def sumargd(gds):
    suma = 0
    for gd in gds:
        try:
            resultado = float(gd.monto)
            suma += resultado
        except (ValueError, TypeError):
            pass  # Manejo de errores si los datos no son válidos

    if suma < 0:
        return "$ {:,.0f} )".format(suma).replace('.', ',').replace(',', '.').replace('-', '( ')
    else:
        return "$ {:,.0f}".format(suma).replace('.', ',').replace(',', '.')            

@register.filter
def multiplicar(monto, multiplicador):
     try:
        resultado = float(monto) * float(multiplicador)
        return "$ {:,.0f}".format(resultado).replace('.', ',').replace(',', '.') 
        
     except ValueError:
         return monto

@register.filter
def multiplicar_y_sumar(operations):
    suma = 0
    for operation in operations:
        try:
            resultado = float(operation.monto) * float(operation.multiplicador)
            suma += resultado
        except (ValueError, TypeError):
            pass  # Manejo de errores si los datos no son válidos

    return "$ {:,.0f}".format(suma).replace('.', ',').replace(',', '.')

