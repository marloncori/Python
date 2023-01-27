# https://www.youtube.com/watch?v=Peq4GCPNC5c&t=2279s
# FreeCodeCamp - 10 Common Coding Interview Problems
# 1 - Valid anagram (29-05-2022) 'danger', 'garden'

# same characters with the same frequency
###########################################################
from collections import Counter

def are_anagrams(first_word, sec_word):
    if len(first_word) != len(sec_word):
        return False
    return Counter(first_word) == Counter(sec_word)

###########################################################
def test_program(input_list):
    result1 = are_anagrams(input_list[0], input_list[1])
    result2 = are_anagrams(input_list[2], input_list[3])
    result3 = are_anagrams(input_list[4], input_list[5])
    return result1, result2, result3

###########################################################
def cleanup():
    print(' User has stopped program execution. Goodbye!')

###########################################################
if __name__ == '__main__':
    try:
        words = ['danger', 'garden', 'Rome', 'amor', 'salesman', 'nameless']
        res1, res2, res3 = test_program(words)
        
        print(f"\n\tAre the words '{words[0]}' and '{words[1]}' anagrams? {res1}")
        print(f"\n\tAnd are the words '{words[2]}' and '{words[3]}' anagrams? {res2}")
        print(f"\n\tAnd are the words '{words[4]}' and '{words[5]}' anagrams? {res3}")
        
    except (KeyboardInterrupt, SystemExit):
        cleanup()
###########################################################