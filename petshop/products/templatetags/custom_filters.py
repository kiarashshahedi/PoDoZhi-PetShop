from django import template

register = template.Library()

@register.filter
def format_price(price):
    # Convert the price to a string
    price_str = str(price)
    
    # Split the price into integer and decimal parts
    if '.' in price_str:
        integer_part, decimal_part = price_str.split('.')
    else:
        integer_part = price_str
        decimal_part = ''
    
    # Reverse the integer part for easier processing
    reversed_integer = integer_part[::-1]
    
    # Add commas every three digits
    grouped_integer = ','.join(reversed_integer[i:i+3] for i in range(0, len(reversed_integer), 3))
    
    # Reverse the integer part back to normal
    formatted_integer = grouped_integer[::-1]
    
    # Combine the formatted integer part with the decimal part if it exists
    if decimal_part:
        return f'{formatted_integer}.{decimal_part}'
    else:
        return formatted_integer



# show discription just 3 words 
@register.filter(name='first_three_words')
def first_three_words(value):
    words = value.split()[:3]
    return ' '.join(words)


# load banner sliders
@register.filter
def group_by_three(value):
    return [value[i:i + 1] for i in range(0, len(value), 1)]

@register.filter
def add_to_list(value, item):
    if item not in value:
        value.append(item)
    return value

@register.filter
def in_list(value, arg):
    return arg in value

@register.filter(name='truncate_words')
def truncate_words(value, num_words):
    words = value.split()
    if len(words) > num_words:
        return ' '.join(words[:num_words]) + '...'
    return value
