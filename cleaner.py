textfile = open('lastOutput.txt', 'r')
lines = textfile.readlines()
textfile.close()

textfile = open('lastOutput.txt', 'w')
for line in lines:
    if '%' in line:
        cleanedLine = line.split('%')[0]
        textfile.write(cleanedLine+'\n')
    elif ';' not in line:
        textfile.write(line+'\n')