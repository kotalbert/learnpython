def is_vovel(character):
    vovels = "aeiouAEIOU"
    for v in vovels:
        if v == character:
            return True
    else:
        return False

def anti_vowel(text):

    letters_list = []
    for letter in text:
        if not is_vovel(letter):
            letters_list.append(letter)

    new_text = "".join(letters_list)
    return new_text

#Testing
chars = ['a', 'b', 'c', 'd', 'e']
for c in chars:
    print c, " is a vovel: ", is_vovel(c)

print anti_vowel("Hey look Words!")
