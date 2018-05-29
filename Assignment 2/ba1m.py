def NumberToSymbol(number):

    if number == 0:
        return 'A'
    elif number == 1:
        return 'C'
    elif number == 2:
        return 'G'
    elif number == 3:
        return 'T'
    
def NumberToPattern(index, k):

    if k == 1:
        return NumberToSymbol(index)
    quotient = index//4
    remainder = index%4
    prefixPattern = NumberToPattern(quotient,k-1)

    return prefixPattern+NumberToSymbol(remainder)
