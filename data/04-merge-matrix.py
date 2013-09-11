
import utils
from itertools import groupby

types = ['dim', 'flag', 'metric']

skey = lambda cell: cell.sortkey.split()[0]
sortedcells = sorted(utils.cells(), key=skey)
for y, (row, cells) in enumerate(groupby(sortedcells, skey)):
    for cell in cells:
        if cell.is_empty:
            continue
        color = types.index(cell.type)
        print '%s %d %d %d %d' % (cell.key,
                                  cell.x,
                                  y,
                                  0 if cell.type == 'flag' else 1,
                                  color)
