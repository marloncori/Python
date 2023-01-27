# https://www.youtube.com/watch?v=Peq4GCPNC5c&t=2279s
# FreeCodeCamp - 10 Common Coding Interview Problems
# 1 - Valid anagram (29-05-2022) 'danger', 'garden'

# same characters with the same frequency
###########################################################
def are_anagrams(first_word, sec_word):
    if len(first_word) != len(sec_word):
        return False
    freq1 = {}
    freq2 = {}
    for ch in first_word:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    for ch in sec_word:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    return True

###########################################################
def test_program(input_list):
    result1 = are_anagrams(input_list[0], input_list[1])
    result2 = are_anagrams(input_list[2], input_list[3])
    return result1, result2

###########################################################
def cleanup():
    print(' User has stopped program execution. Goodbye!')

###########################################################
if __name__ == '__main__':
    try:
        words = ['danger', 'garden', 'Rome', 'amor']
        res1, res2 = test_program(words)
        
        print(f"\n\tAre the words '{words[0]}' and '{words[1]}' anagrams? {res1}")
        print(f"\n\tAnd are the words '{words[2]}' and '{words[3]}' anagrams? {res2}")
        
    except (KeyboardInterrupt, SystemExit):
        cleanup()
###########################################################