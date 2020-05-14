def to(number, ff):
    string = ''
    while number != 0:
        remainder = number % ff
        number = number // ff
        string = str(remainder) + string
    return string
dec=int(input())
print({'bin': to(dec, 2), 'oct': to(dec, 8),
       'hex': to(dec, 16), 'chr': chr(dec), })
