
letterScores = {}

def initiateLetterScores():
    letterScores = {"-":0,"aeioulnrst":1,"dg":2,"bcmp":3,"fhvwy":4,"k":1,"jx":8,"qz":10}
    return letterScores


def computeScore(word,letterScores):
    sum = 0
    print letterScores
    for i in word:
        for j in letterScores.keys():
           if i in j:
                sum = sum + letterScores[j]
    return sum

print(computeScore("idiot",initiateLetterScores()))
