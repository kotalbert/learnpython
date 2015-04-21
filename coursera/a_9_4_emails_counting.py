# name = raw_input("Enter file:")
# 
# if len(name) < 1 : name = "mbox-short.txt"

handle = open("mbox-short.txt")
counts = dict()

for line in handle:
    if not line.startswith("From ") : continue
    
    words = line.split()
    mail = words[1]
    
    counts[mail] = counts.get(mail,0) + 1

max_key = None

for k in counts:
    if max_key is None:
        max_key = k
        continue
    
    if counts[k] > counts[max_key]:
        max_key = k 
    
print max_key, counts[max_key]
    