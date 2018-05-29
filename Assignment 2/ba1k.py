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

def ComputingFrequencies(text, k):

    frequencyArray = [0]*(4**k)
    
    for i in range (len(text)-(k-1)):

        frequencyArray [PatternToNumber(text[i:i+k])] +=1

    return frequencyArray

