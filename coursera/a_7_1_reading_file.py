# Use words.txt as the file name

fname = raw_input("Enter file name: ")
f = open(fname, 'r')

for line in f:
    print line.upper().strip()
    
f.close()