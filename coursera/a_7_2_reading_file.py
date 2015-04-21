# Use words.txt as the file name

# Use the file name mbox-short.txt as the file name
# fname = raw_input("Enter file name: ")
# fh = open(fname)

fh = open("mbox-short.txt")

conf = 0.0
conf_sum = 0.0
conf_count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    
    conf = float(line[line.find("0."):])
    conf_count += 1
    conf_sum += conf
    
conf_avg = conf_sum / conf_count

print "Average spam confidence:", conf_avg

fh.close()
    
    
