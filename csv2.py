inFile = open('team_dedup.csv','r')

outFile = open('2.csv','w')

listLines = []

for line in inFile:

    if line in listLines:
        continue

    else:
        outFile.write(line)
        listLines.append(line)

outFile.close()

inFile.close()