import re
from collections import Counter
import numpy as np
import pandas as pd
import nltk
from utils import extract_features

nltk.download('twitter_samples')
nltk.download('stopwords')

#@title Q1 Process Data

def process_data(file_name):
    """
    Input:
        A file_name which is found in your current directory. You just have to read it in.
    Output:
        wordprobs: a dictionary where keys are all the processed lowercase words and the 
             values are the frequency that it occurs in the corpus (text file you read).
    """
    words = [] # return this variable correctly

     ### START CODE HERE ###

    #Open the file, read its contents into a string variable
    with open(file_name, "r", encoding = "utf-8") as f:
        data = f.read()
    

    # convert all letters to lower case
    lower_case_data = data.lower()

    # with words as keys, ensure that we have a count of their occurrences
    words_prob = {}
    words_list = re.findall(r"\w+", lower_case_data)
    total_words = len(words_list)
    words_cnt = Counter(words_list)

    for word, cnt in words_cnt.items():
        words_prob[word] = cnt / total_words
        
    ### END CODE HERE ###

    return words_prob

def process_data_test():

    probs = process_data('./shakespeare-7k.txt')
    assert np.allclose(probs['thee'], 0.004476442720185026), \
                      "expected \"thee\" frequency of 0.004476442720185026"
    assert len(probs) == 6116, "vocabulary should have total of 6116 words.\n\t" + \
        f"length of vocabulary in your implementation is {len(probs)}"

    # Check maximum frequency word
    max_word = ""; max_freq = 0.0
    for word in probs:
      assert word == word.lower(), "all words must be lowercase.\n\t" + \
          f"word \"{word}\" is not lowercase"
      if probs[word] > max_freq:
        max_freq = probs[word]
        max_word = word
    assert max_word == 'the', "\"the\" should be the most frequent word\n\t" + \
        f"your maximum word is \"{max_word}\""
    assert np.allclose(max_freq, 0.028444063117842356)

    print("process_data: \033[1;32mtests OK.\033[0m")



#@title Q2: N-gram most likely next words

def probable_substitutes(word, probs, maxret = 10):
    """
    Determine the most probable words for a misspelled string that are TWO edits
    away. The edits that are possible are:

        * delete_letter: removing a character
        * switch_letters: switching two adjacent characters
        * replace_letter: replacing one character by another different one
        * insert_letter: inserting a character

    There may be fewer but no more than maxret words.

    Input:
        word - The misspelled word
        probs - A dictionary of word --> prob
        maxret - Maximum number of words to return
    Returns:
        Tuples of the words and their probabilities, ordered by highest frequency.
        [(word1, prob1), ... ]
    """
    # <YOUR-CODE-HERE>
    def one_edit(word):
        letters = 'abcdefghijklmnopqrstuvwxyz'

        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]

        # delete_letter
        deletes = [L + R[1:] for L, R in splits if R]
        
        # switch_letters
        switches = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]

        # replace_letter
        replaces = [L + c + R[1:] for L, R in splits if R
                                  for c in letters if c != R[0]
                   ]

        # insert_letter
        inserts = [L + c + R for L, R in splits 
                             for c in letters
                  ]
        return set(deletes + switches + replaces + inserts)
        
    # exactly two edits
    edit_once = one_edit(word)
    edit_twice = set()
    for w in edit_once:
        edit_twice.update(one_edit(w))

    probable_substitutes_result = []
    for w in edit_twice:
        if w in probs:
            probable_substitutes_result.append((w, probs[w]))

    probable_substitutes_result.sort(key = lambda x:(-x[1], x[0]))
    
    return probable_substitutes_result[:maxret]
    

def probable_substitutes_test():
    probs = dict()
    probs['raid'] = 0.25
    probs['rain'] = 0.1
    probs['raise'] = 0.1
    probs['void'] = 0.15
    probs['roid'] = 0.20
    probs['rein'] = 0.2

    # Check delete one add one
    probable_substitutes_result = probable_substitutes('braid', probs, maxret = 5)   
    probable_substitutes_expected = [('raid', 0.25), ('roid', 0.2), ('rain', 0.1)]
    assert probable_substitutes_result == probable_substitutes_expected, \
      str(probable_substitutes_expected) + "\n\tReceived" + str(probable_substitutes_result)
    
    # Check insert two
    probable_substitutes_result = probable_substitutes('id', probs, maxret = 5)   
    probable_substitutes_expected = [('raid', 0.25), ('roid', 0.2), ('void', 0.15)]
    assert probable_substitutes_result == probable_substitutes_expected, \
      str(probable_substitutes_expected) + "\n\tReceived" + str(probable_substitutes_result)

    print("probable_substitutes: \033[1;32mtests OK.\033[0m")

#@title Q3: The Minimum Edit Distnance

def min_edit_distance(source, target, ins_cost = 1, 
                      del_cost = 1, rep_cost = 2):
    '''
    Input:
        source: starting string
        target: ending string
        ins_cost: integer representing insert cost
        del_cost: integer representing delete cost
        rep_cost: integer representing replace cost
    Output:
        D: matrix of size (len(source)+1 , len(target)+1) 
           with minimum edit distances
        med: the minimum edit distance required to convert
             source to target
    '''
    # <YOUR-CODE-HERE>
    len_source = len(source)
    len_target = len(target)
    D = [[0 for _ in range(len_target + 1)] for _ in range(len_source + 1)]

    for j in range(1, len_target + 1):
        D[0][j] = D[0][j - 1] + ins_cost
        
    for i in range(1, len_source + 1):
        D[i][0] = D[i - 1][0] + del_cost
        
    for i in range(1, len_source + 1):
        for j in range(1, len_target + 1):
            if source[i - 1] == target[j - 1]:
                D[i][j] = min(D[i - 1][j] + del_cost, D[i][j - 1] + ins_cost, D[i - 1][j - 1]) 
            else:
                D[i][j] = min(D[i - 1][j] + del_cost, D[i][j - 1] + ins_cost, D[i - 1][j - 1] + rep_cost) 

    med = D[len_source][len_target]
    
    return D, med

def min_edit_distance_test():

    matrix, mindist = min_edit_distance("hello", "help", ins_cost = 1, del_cost = 1, rep_cost = 2)
    assert mindist == 3, "Expected distance of 3, but received: " + str(mindist)   

    matrix, mindist = min_edit_distance("hello", "jello", ins_cost = 1, del_cost = 1, rep_cost = 2)
    assert mindist == 2, "Expected distance of 2, but received: " + str(mindist)

    matrix, mindist = min_edit_distance("ello", "jello", ins_cost = 1, del_cost = 1, rep_cost = 2)
    assert mindist == 1, "Expected distance of 1, but received: " + str(mindist)

    print("min_edit_distance: \033[1;32mtests OK.\033[0m")

def bpe_learn_merges(corpus, num_merges=5):
    '''
    Input:
    corpus: string containing space-separated words
    num_merges: integer specifying how many merge operations to learn
    Output:
    merges: list of tuples (pair_symbol_1, pair_symbol_2) ordered by learning sequen
    vocab: dict of final vocabulary tokens and their frequencies
    '''
    # Initialize vocabulary
    word_cnts = Counter(corpus.split())

    vocab = {}

    for word, cnt in word_cnts.items():
        tokens = tuple(word) + ('</w>',)
        vocab[tokens] = cnt

    merges = []
    # Repeat BPE merges
    for _ in range(num_merges):
        # Count adjacent token pairs
        pair_cnts = Counter()
    
        for tokens, cnt in vocab.items():
            for i in range(len(tokens) - 1):
                pair = (tokens[i], tokens[i + 1])
                pair_cnts[pair] += cnt
                
        # Stop if no adjacent pairs remain
        if not pair_cnts:
            break
            
        # find the most frequent pair
        best_pair = min(pair_cnts, key = lambda pair: (-pair_cnts[pair], pair))
        merges.append(best_pair)
        
        # merge
        new_vocab = {}
    
        for tokens, cnt in vocab.items():
            new_tokens = []
    
            i = 0
            while i < len(tokens):
                if i < len(tokens) - 1 and (tokens[i], tokens[i + 1]) == best_pair:
                    new_tokens.append(tokens[i] + tokens[i + 1])
                    i += 2
                else:
                    new_tokens.append(tokens[i])
                    i += 1
    
            new_tokens = tuple(new_tokens)
            new_vocab[new_tokens] = new_vocab.get(new_tokens, 0) + cnt
    
        vocab = new_vocab

    return merges, vocab

if __name__ == '__main__':

    print("Running unit tests ... ")
    process_data_test()
    probable_substitutes_test()
    min_edit_distance_test()

    print("Processing data, assuming that shakespeare-7k.txt is in working directory...")
    probs = process_data('./shakespeare-7k.txt')

    print("\n\nLet's try autocorrect. \"(Q)/(q)uit\" to end.")
    entry = input("Enter any word:")
    entry = entry.lower()
    while not entry == "q" and not entry == 'quit':
        print(probable_substitutes(entry, probs, maxret = 5))
        entry = input("Enter any word:")
        entry = entry.lower()

    print("\n\nLet's try min edit distance.")
    while not entry == 'n' and not entry == 'no':
        source = input("Enter any source word:")
        source = source.lower()
        target = input("Enter any target word:")
        target = target.lower()
        D, d = min_edit_distance(source, target)
        print(source, " and ", target, " are ", d, " apart")
        entry = input("Continue? (Y/y)es / (N/n)o:")

    print("\n\nLet's try BPE Tokenization. \"(Q)/(q)uit\" to end.")
    corpus = input("Enter a corpus (space-separated words): ")
    while corpus.lower() not in ("q", "quit"):
        num_merges = int(input("Enter number of merges (default 5): ") or 5)
        merges, vocab = bpe_learn_merges(corpus, num_merges)
        print("\nLearned merges:")
        for i, pair in enumerate(merges, 1):
            print(f"{i}. {pair}")
        print("\nFinal vocabulary:")
        for tokens, freq in vocab.items():
            print(f"{tokens}: {freq}")
        corpus = input("\nEnter a corpus (or Q to quit): ")