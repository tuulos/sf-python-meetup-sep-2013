
import utils
from itertools import groupby

types = ['dim', 'flag', 'metric']

skey = lambda cell: cell.sortkey.split()[0]
sortedcells = sorted(utils.cells(), key=skey)
for y, (_row, cells) in enumerate(groupby(sortedcells, skey)):
    for i, (_row, cells) in enumerate(groupby(cells, lambda cell: cell.y)):
        x = 0
        for cell in cells:
            if cell.is_empty:
                continue
            color = 3 if i > 0 else types.index(cell.type)
            print '%s %d %d %d %d' % (cell.key,
                                      x,
                                      y,
                                      0 if cell.type == 'flag' else 1,
                                      color)
            x += 1
