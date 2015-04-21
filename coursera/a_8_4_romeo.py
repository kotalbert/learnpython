# fname = raw_input("Enter file name: ")
fname = "romeo.txt"
fh = open(fname)
lst = list()

def add_to_list(words):
    for word in words:
        if word not in lst:
            lst.append(word)


for line in fh:
    words = line.split()
    add_to_list(words)
    lst.sort()
    
print lst