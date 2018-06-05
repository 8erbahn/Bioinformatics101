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

