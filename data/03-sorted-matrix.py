import utils
from itertools import groupby

types = ['dim', 'flag', 'metric']

sortedcells = sorted(utils.cells(), key=lambda cell: cell.sortkey)
for y, (_row, cells) in enumerate(groupby(sortedcells, lambda cell: cell.sortkey)):
    for cell in cells:
        if cell.is_empty:
            continue
        color = types.index(cell.type)
        print '%s %d %d %d %d' % (cell.key,
                                  cell.x,
                                  y,
                                  0 if cell.type == 'flag' else 1,
                                  color)

