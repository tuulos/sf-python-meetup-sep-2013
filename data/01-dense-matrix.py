import utils

for cell in utils.cells():
    if cell.is_empty:
        continue
    print '%s %d %d 1 0' % (cell.key, cell.x, cell.y)

