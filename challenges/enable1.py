'''
This challenge was acquired from:
    https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/
'''

def letter_sum(word) -> int:
    '''
    Return the sum of the value of each letter in a word.
    Value of a letter is determined by its position in the alphabet.
    Ex. A = 1, B = 2, C = 3, and so on. 
    '''
    BASE = 96
    if len(word) == 1:
        return ord(word) - BASE
    return ord(word[0]) - BASE + letter_sum(word[1:])  # My attempt at recursion


def make_words_sums(words):
    '''Return a dictionary of each word and its respective letter sum.'''
    return {word: letter_sum(word) for word in words}


# Find the word(s) with letter sum of n
def words_with_sum_n(words:dict, n) -> list:
    '''Return a list of words that sum to n.'''
    return [k for k, v in words.items() if v == n]


# Find the word(s) with letter sum of n
def words_with_sum(words:list, n) -> list:
    '''Return a list of words that sum to n.'''
    return [w for w in words if letter_sum(w) == n]


# Query a dictionary by it's values
def filter_values(words:dict, my_func):
    '''
        Apply a function on the values to query the dictionary.
        Return a list of the resulting values.'''
    return [my_func(v) for v in words.values() if my_func(v) is not None]


def filter_keys(words:dict, my_func):
    '''
        Apply a function on the keys to query the dictionary.
        Return a list of the resulting keys.'''
    return [my_func(k) for k in words.keys() if my_func(k) is not None]

   
# Find the total number of words whose letter sum is odd
def count_odd_letter_sum(words) -> int:
    '''Return the total count of words whose letter sum is odd.'''
    count = 0
    for word in words:
        if letter_sum(word) % 2 != 0:
            count += 1
    return count


# Find the number of words for each available letter sums.
def get_word_sizes(words:list) -> dict:
    '''Return a count of the number of words for each letter sum.'''
    a = {}
    for word in words:
        try:
            a[letter_sum(word)] += 1
        except:
            a.setdefault(letter_sum(word), 1)
    return a


# Find the number of words for each available letter sums. 
def get_word_sizes_2(words:dict) -> dict:
    '''Return a count of the number of words for each letter sum.'''
    _list = list(words.values())
    _set = set(_list)
    return {i: _list.count(i) for i in _set}


# Sort word_sizes by converting to list of key, value pairs
def make_pairs(dic):
    '''Convert a dictionary to a list of tuples.'''
    return list(dic.items())


def sort_pairs(pairs, i, reverse=False):
    '''Sort by the ith index of each tuple.'''
    # Sort each tuple by ith index 
    if reverse:
        pairs.sort(key=lambda x: x[i], reverse=True)
    pairs.sort(key=lambda x: x[i])
    return pairs


# Get the list of words
filename = 'enable1.txt'
with open(filename) as f:
    words = [word.strip() for word in f.readlines()]

# Turn the list of words into keys with their letter sums as values
words_sums = make_words_sums(words)

# Question # 1: Find the only word with a letter sum of 319.
n = 319
filter_keys(words_sums, lambda x: x if letter_sum(x) == n else None) 
words_with_sum_n(words_sums, n)
words_with_sum(words, n)

# Question # 2: How many words have an odd letter sum?
len(filter_values(words_sums, lambda x: x if x % 2 != 0 else None))
count_odd_letter_sum(words)

# Question # 3: What letter sum is most common, and how many words have it?
word_sizes = get_word_sizes_2(words_sums)
pairs = make_pairs(word_sizes)
pairs = sort_pairs(pairs, 1)    # Sort by y in each (x, y) pair.
pairs[-1]   # 93 letter sum is the most common; 1965 words have it.


# Question # 4: Find the pair of words that have the same letter sum but difference in word length of n.
def get_same_sums(words, n):
    '''Return a list of words with the same letter sums.'''
    return filter_keys(words, lambda x: x if words[x] == n else None)


def diff_in_len(a, b):
    '''Return the absolute value in the difference of length of 2 words.'''
    return abs(len(a) - len(b))


set_of_sums = list(set(words_sums.values()))
same_sums_w_difference = []
DIFFERENCE = 11
for _sum in set_of_sums:
    same_sums = get_same_sums(words_sums, _sum) # create a list of words with the same letter sum
    for i, word in enumerate(same_sums):
        if word == same_sums[-1]:
            break
        for second_word in same_sums[i+1:]:
            if diff_in_len(word, second_word) == DIFFERENCE:
                same_sums_w_difference.append((word, second_word))



# 5. Find a pair of words that have no letters in common, and that have the same letter sum.
same_sums_no_same_letters = []  # each element will be a pair of 2 words


def have_same_letters(a, b):
    '''Returns true if two words a and b have at least one sharing letter.'''
    for c in a:
        if c in b:
            return True
    return False

# Reusing code from above because this is just a challenge, 
# and I think I have exhausted myself with use of functions, for now.
for _sum in set_of_sums[186:]:
    same_sums = get_same_sums(words_sums, _sum) # create a list of words with the same letter sum
    for i, word in enumerate(same_sums):
        if word == same_sums[-1]:
            break
        for second_word in same_sums[i+1:]:
            if not have_same_letters(word, second_word):
                same_sums_no_same_letters.append((word, second_word))