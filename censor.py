def censor(text, word):
    split_text = text.split()
    
    
    #Replace censored words
    for i in range(0, len(split_text)):
        if split_text[i] == word:
            split_text[i] = "*"*len(word)
            
    return " ".join(split_text)

#Testing
def test_print(text, word):
    print "Text: %s, Word: %s, Output: %s"  % (text, word, censor(text, word))
#    "Text: ", s, ", output: " , censor(s)
    
test_print("this hack is wack hack", "hack")

test_print("hey hey hey","hey")

test_print("Yo go fro yo go","go")