import nltk
from nltk.corpus import wordnet

def propose_words(sentence):
    # Split the sentence into words
    words = nltk.word_tokenize(sentence)
    
    # Find the index of the blank (indicated by the word word)
    blank_index = words.index('etc')
    
    # Get the part of speech of the word before the blank
    pos = nltk.pos_tag([words[blank_index-1]])[0][1]
    
    # Get synonyms of the word before the blank that have the same part of speech
    synonyms = wordnet.synsets(words[blank_index-1], pos=pos)
    
    # Get the lemmas (base form of the word) of the synonyms
    lemmas = [s.lemmas()[0].name() for s in synonyms]
    
    # Remove the word before the blank from the list of lemmas
    lemmas = [lemma for lemma in lemmas if lemma != words[blank_index-1]]
    
    # Return the first seven lemmas as proposed words
    return lemmas[:7]

# Test the function with a sample sentence
sentence = "The cat sat on the etc."
print(propose_words(sentence))
