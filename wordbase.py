
import string
import trie

# words = ['abc', 'abcdye', 'bed', 'dey', 'xe']

words = {}
for letter in list(string.ascii_lowercase):
    with open('dict/%s.txt' % letter) as f:
        content = f.readlines()
        for word in content:
            words[word.strip()] = True

word_trie = trie.make_trie(words.keys())

# grid = [
#     ['a', 'b', 'd', 'f'],
#     ['e', 'c', 'e', 'f'],
#     ['x', 'd', 'y', 'f'],
# ]

# 10x13
grid = [
    ['u', 'n', 's', 'i', 'k', 't', 'b', 'e', 'j', 'o'],
    ['i', 'a', 'm', 'n', 's', 'r', 'i', 'c', 'g', 'b'],
    ['v', 't', 'p', 'a', 'o', 'f', 't', 'g', 'e', 'h'],
    ['c', 'p', 'l', 'i', 'y', 'o', 'n', 'i', 'm', 'a'],
    ['w', 'i', 'n', 's', 'c', 'u', 's', 't', 'l', 's'],
    ['a', 'n', 'g', 'l', 'e', 's', 'i', 'y', 'e', 'n'],
    ['k', 'y', 'i', 'y', 's', 't', 'c', 'o', 'v', 'r'],
    ['r', 'e', 's', 'a', 'r', 's', 'o', 'b', 'a', 'l'],
    ['s', 'p', 'n', 'u', 'b', 'e', 'a', 'n', 'e', 'c'],
    ['t', 'o', 'r', 't', 'h', 'm', 't', 'l', 'r', 'i'],
    ['r', 's', 'd', 'u', 'o', 's', 'i', 'y', 'l', 'b'],
    ['b', 'e', 's', 'h', 'l', 'e', 'a', 'n', 'e', 'u'],
    ['s', 'n', 'p', 't', 'e', 'm', 'r', 'y', 'r', 'k'],
]

start_locations = [
    (0, 0),
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (0, 5),
    (0, 6),
    (0, 7),
    (0, 8),
    (0, 9),
    (1, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (1, 5),
    (1, 6),
]

# These directions assume player position is at the top of
# the grid.

N = [0, -1]
S = [0, 1]
E = [1, 0]
W = [-1, 0]
NE = [1, -1]
NW = [-1, -1]
SE = [1, 1]
SW = [-1, 1]

directions = [NW, N, W, SW, S, E, NE, SE]

height = len(grid)
width = len(grid[0])

print 'board: %dx%d' % (width, height)

def out_of_bounds(x, y):
    return not (x >= 0 and y >= 0 and x < width and y < height)

def intersect(xs, ys):
    ht = {}
    result = []
    for x in xs:
        ht[x] = True
    for y in ys:
        if y in ht:
            result.append(y)
    return result

def all_words(grid, x, y, (current_word, current_score)=('', 0), been={}):
    if len(current_word) > 10:
        return []

    # print current_word

    current_letter = grid[y][x]
    current_word = current_word + current_letter
    current_state = (current_word, max(current_score, y))
    been[(x, y)] = True

    grid_neighbours = []
    for [dx, dy] in directions:
        nx = x + dx
        ny = y + dy
        if not out_of_bounds(nx, ny) and (nx, ny) not in been:
            grid_neighbours.append((nx, ny))

    neighbouring_letters = [grid[y][x] for (x, y) in grid_neighbours]

    result = []

    (in_dictionary, neighbours) = trie.in_trie_neighbours(word_trie, current_word)

    if in_dictionary:
        result.append(current_state)

    if not intersect(neighbours, neighbouring_letters):
        return result

    for (nx, ny) in grid_neighbours:
        result = result + all_words(grid, nx, ny, current_state, been.copy())

    return result

# This indicates whether player position is at the top. If it's
# not, it flips the grid, so the earlier assumption stays valid.

down = False

g = grid if down else grid[::-1]

print(all_words(g, 2, 0))
# print(sum([all_words(g, x, y) for (x, y) in start_locations], []))
