from random import randint

def RandomizedMotifSearch (dna, k, t):
        SetofStrings = dna.split()
        FirstMotif = [0]*len(SetofStrings)
            

        for i in range (0, t):

            kmer = SetofStrings[i]
            randomNumber = randint(0,len(kmer)-k)
            FirstMotif[i] = kmer[randomNumber:randomNumber+k]

        bestMotif = FirstMotif
        profile = GetProfile(FirstMotif)

        while True:
            
            motif = GetMotif(profile, SetofStrings, k)
            profile = GetProfile(motif)

            if (GetScore(GetProfile(bestMotif), motif)) < (GetScore(GetProfile(bestMotif),bestMotif)):

                bestMotif = motif
                
            else:
                    
                return bestMotif


    


def GetProfile(motif):

    k = len(motif[0])
    countA = [1.0]*k
    countC = [1.0]*k
    countG = [1.0]*k
    countT = [1.0]*k

    for i in range(0, len(motif)):

        for a in range (0, k):

            if motif[i][a] == "A":
                countA[a] += 1
            if motif[i][a] == "C":
                countC[a] += 1
            if motif[i][a] == "G":
                countG[a] += 1
            if motif[i][a] == "T":
                countT[a] += 1
    profileA = countA
    profileC = countC
    profileG = countG
    profileT = countT

    for b in range(0,k):

        profileA[b] = profileA[b]/(len(profileA)+4)
        profileC[b] = profileC[b]/(len(profileA)+4)
        profileG[b] = profileG[b]/(len(profileA)+4)
        profileT[b] = profileT[b]/(len(profileA)+4)
        
    return (profileA,profileC,profileG,profileT)



    
def GetMotif(profil, SetofDNAStrings, k):

    bestprobability = 0
    finalMotif = [0]*len(SetofDNAStrings)

    for i in range (0, len(SetofDNAStrings)):

        bestkmer = ""
        bestprobability = 0

        for h in range (0, len(SetofDNAStrings[i])-k):

            probability = 1

            kmer = SetofDNAStrings[i][h:h+k]

            for g in range (0, len(kmer)):

                if kmer[g] == 'A':
                    probability = probability * profil[0][g]
                if kmer[g] == 'C':
                    probability = probability * profil[1][g]
                if kmer[g] == 'G':
                    probability = probability * profil[2][g]
                if kmer[g] == 'T':
                    probability = probability * profil[3][g]
            if probability > bestprobability :
                bestkmer = kmer
                bestprobability = probability
                
            finalMotif[i] = bestkmer
            
    return finalMotif


def GetScore (profile, motif):

    consensus = ""
    score = 0

    for i in range (0, len(motif[0])):

        highestprobability = 0

        if profile[0][i] > highestprobability:
            highestprobability = profile[0][i]
            a = "A"
        if profile[1][i] > highestprobability:
            highestprobability = profile[1][i]
            a = "C"
        if profile[2][i] > highestprobability:
            highestprobability = profile[2][i]
            a = "G"
        if profile[3][i] > highestprobability:
            highestprobability = profile[3][i]
            a = "T"
        consensus += a

    for i in range (0, len(motif)):

        score += HammingDistance(motif[i], consensus)

    return score
    


def HammingDistance (dna, consensus):

    count = 0

    for i in range(0, len(dna)):

        if dna[i] != consensus[i]:

            count =count + 1

    return count
