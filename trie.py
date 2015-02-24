
_end = '_end_'

def make_trie(words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict = current_dict.setdefault(_end, _end)
    return root

def in_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter in current_dict:
            current_dict = current_dict[letter]
        else:
            return False
    else:
        if _end in current_dict:
            return True
        else:
            return False

def in_trie_neighbours(trie, word):
    ''' Returns a tuple of whether a word is in the trie, and its neighbours '''
    current_dict = trie
    for letter in word:
        if letter in current_dict:
            current_dict = current_dict[letter]
        else:
            return (False, [])
    else:
        if _end in current_dict:
            return (True, [key for key in current_dict.keys() if key != _end])
        else:
            return (False, current_dict.keys())

if __name__ == '__main__':
    t = make_trie(['cat', 'catamorphic'])
    print t
    print in_trie_neighbours(t, 'cat')
    print in_trie_neighbours(t, 'catamo')
    print in_trie_neighbours(t, 'catamorphic')
