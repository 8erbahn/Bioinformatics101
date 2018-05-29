def PatternToNumber(pattern):

    if pattern == "" :
        return 0

    lastSymbol = pattern[-1]
    restOfPattern = pattern[0:-1]

    return (4*PatternToNumber(restOfPattern)+SymbolToNumber(lastSymbol))

def SymbolToNumber(symbol):

    if symbol == 'A':
        return 0
    elif symbol == 'C':
        return 1
    elif symbol == 'G':
        return 2
    elif symbol == 'T':
        return 3

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

def ComputingFrequencies(text, k):

    frequencyArray = [0]*(4**k)
    
    for i in range (len(text)-(k-1)):

        frequencyArray [PatternToNumber(text[i:i+k])] +=1

    return frequencyArray

def FasterFrequentWords (text, k):

    frequentPatterns = []
    frequencyArray = ComputingFrequencies(text, k)

    maxCount = max(frequencyArray)

    for a in range (0, len(frequencyArray)-1):

        if frequencyArray[a] == maxCount:

            pattern = NumberToPattern(a,k)

            if pattern not in frequentPatterns:

                frequentPatterns.append(pattern)

    print (frequentPatterns)
    


        


