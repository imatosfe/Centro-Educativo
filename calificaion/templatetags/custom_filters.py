from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return None  # O cualquier valor predeterminado si no existe la clave
