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
    _base = 96
    if len(word) == 1:
        return ord(word) - _base
    return ord(word[0]) - _base + letter_sum(word[1:])  # My attempt at recursion


# Find the word with letter sum of 319
def words_with_sum(words, n) -> list:
    '''Return a list of words that sum to n.'''
    result = []
    for word in words:
        if letter_sum(word) == n:
            result.append(word)
    return result


# Find the total number of words whose letter sum is odd
def count_odd_letter_sum(words) -> int:
    '''Return the total count of words whose letter sum is odd.'''
    count = 0
    for word in words:
        if letter_sum(word) % 2 != 0:
            count += 1
    return count


# Find the number of words for each available letter sums.
# Work in Progress...
def word_sizes(words) -> dict:
    '''Return a count of the number of words for each letter sum.'''
    a = {}
    for word in words:
        try:
            a[letter_sum(word)] += 1
        except:
            a.setdefault(letter_sum(word), 1)
    return a


with open('enable1.txt', 'r') as f:
    words = [word.strip() for word in f.readlines()]

a = word_sizes(words)

highest_k = 0
highest_v = 0
for k, v in a.items():
    if v > highest_v:
        highest_v = v
        highest_k = k