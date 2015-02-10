def reverse(text):
    i = len(text)
    result = ""

    while i > 0:
        result += text[i-1]
        i -= 1
    return result

#testing function
textes = ["ABC", "XYZ", "Help me!"]

for t in textes:
    print "Testing: %s" %t, "reversed: ", reverse(t)
    
