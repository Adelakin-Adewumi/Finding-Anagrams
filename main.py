# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def is_anagram(word1, word2):
    if (sorted(word1) == sorted(word2)):
        return True
    else:
        return False
print(is_anagram("keen", "neek"))
    # [assignment] Add your code here

    # return True

