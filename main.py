# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

import string

word = input("Write the first word here: ")
anagram = input("Write the second word here to check for anagram: ")

def find_anagram(word, anagram):
    # [assignment] Add your code here

    word = "".join(word.split(" ")).lower()
    anagram = "".join(anagram.split(" ")).lower()

    word = word.translate(str.maketrans('','',string.punctuation))
    anagram = anagram.translate(str.maketrans('','',string.punctuation))
   
    if sorted(word) == sorted(anagram):
        return True
    else:
        return False

print(find_anagram(word, anagram))