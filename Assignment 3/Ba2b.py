def HammingDistance (dna, consensus):

    count = 0

    for i in range(0, len(dna)):

        if dna[i] != consensus[i]:

            count =count + 1

    return count

def DistanceBetweenPatternAndString(pattern, dna):

    k = len(pattern)
    distance = 0

    stringSet = dna.split()

    for i in range (0, len(stringSet)):

        Hamming = len(stringSet[i])+1
        tester = stringSet[i]

        for h in range(0, len(tester)-k+1):

            if Hamming > HammingDistance(tester[h:h+k], pattern):

                Hamming = HammingDistance(tester[h:h+k], pattern)
            
        distance = distance + Hamming
    return distance

def medianString (dna, k):

    distance = len(dna)+1

    for i in range(0, 4**k-1):

        pattern = NumberToPattern(i, k)

        if distance > DistanceBetweenPatternAndString(pattern, dna):

            distance = DistanceBetweenPatternAndString(pattern, dna)
            median = pattern
    return median


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
