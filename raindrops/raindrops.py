def convert(number):
    result = ''
    if has_a_factor(3, number):
        result = 'Pling'
    
    if has_a_factor(5, number):
        result += 'Plang'
    
    if has_a_factor(7, number):
        result += 'Plong'
    
    if result == '':
        result = str(number)
    
    return result

def has_a_factor(divisor, number):
    return number % divisor == 0