from collections import namedtuple

Cell = namedtuple('Cell', ['key', 'x', 'y', 'type', 'is_empty', 'sortkey'])

def cells():
    types = ['dim', 'flag', 'metric']
    for i, row in enumerate(open('matrix.txt')):
        dims, flags, metrics = sections = row.split()
        j = 0
        sortkey = '%s %s' % (flags, dims)
        for stype, sect in zip(types, sections):
            for field in sect.split(','):
                yield Cell('e-%d-%d' % (j, i),
                           j,
                           i,
                           stype,
                           field == '' or field == '0',
                           sortkey)
                j += 1
