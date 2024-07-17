from django import template

register = template.Library()

@register.filter
def currency_format(value):
    return "${:,.2f}".format(value)

@register.filter
def multiplicar(monto, multiplicador):
    try:
        resultado = float(monto) * float(multiplicador)
        #return f"$ {resultado:.0f}"
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