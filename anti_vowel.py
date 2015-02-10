def anti_vowel(text):
    vovels = "aeiouAEIOU"
    text_list = list(text)
    
    for letter in text_list:
        for vovel in vovels:
            if letter == vovel:
                #remove from text_list
                index = text_list.index(letter)
                #text_list.remove(index)
                print index
        
    new_text = "".join(text_list)   
    return new_text

#testing function
textes = ["ABCDEFG", "QWERETYUIOP", "Help me!"]

for t in textes:
    print "Testing: %s" %t, "anti_vowel: ", anti_vowel(t)
    
