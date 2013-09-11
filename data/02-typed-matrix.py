import utils

types = ['dim', 'flag', 'metric']

for cell in utils.cells():
    if cell.is_empty:
        continue
    color = types.index(cell.type)
    print '%s %d %d %d %d' % (cell.key,
                              cell.x,
                              cell.y,
                              0 if cell.type == 'flag' else 1,
                              color)

