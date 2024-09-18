'''
Michelle Zhu
Boas
SoftDev
K05 -- bitstream
2024-09-17
time spent: 0.5
'''

def makeRoster (filename):
    data = open(filename).read()
    tuples = data.rsplit("@@@")[:-1]
    names = []
    information = []
    
    for i in range(len(tuples)):
        tuples[i] = tuples[i].rsplit("$$$")
        names.append(tuples[i][1])
        information.append([tuples[i][0],tuples[i][2]])
        
    
    print(roster)

makeRoster(krewes)
        


