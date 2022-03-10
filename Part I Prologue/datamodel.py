rank = [str(n) for n in range(2,11)] + list('JQKA')

rank

suits = 'spades diamonds clubs hearts'.split()

suits

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

Card