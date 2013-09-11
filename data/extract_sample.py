import gzip
import random

NUM_LINES = 200
NUM_METRICS = 10
NUM_CONSECUTIVE = (1, 5)
NUM_INBETWEEN = 1000

def load_columns():
    min_metric = 0
    min_dim = 0
    for i, l in enumerate(l for l in open('columns') if l.strip() and l[0] != '#'):
        if min_metric == 0 and l.startswith('m_'):
            min_metric = i
        if min_dim == 0 and l.startswith('d_'):
            min_dim = i
    return min_metric, min_dim

def rows():
    lines = iter(gzip.GzipFile('data.txt.gz'))
    def next_line():
        line = lines.next()
        fields = line.split('|')
        flags = fields[:min_dim]
        dims = fields[min_dim:min_metric]
        metrics = map(int, (x if x else 0 for x in fields[min_metric:]))
        return dims, flags, metrics

    min_metric, min_dim = load_columns()
    fast_forward = 0
    with_metrics = 0
    num_lines = 0
    while num_lines < NUM_LINES:
        dims, flags, metrics = next_line()
        n = random.randint(*NUM_CONSECUTIVE)
        if with_metrics < NUM_METRICS:
            if sum(metrics[:-1]):
                for _ in range(n):
                    num_lines += 1
                    with_metrics += 1
                    yield next_line()
        else:
            for _ in range(n):
                num_lines += 1
                yield next_line()
        for _ in range(NUM_INBETWEEN):
            next_line()

def nonempty_rows():
    unfiltered = list(rows())
    nonempty = [set() for i in range(3)]
    for sections in unfiltered:
        for j, sect in enumerate(sections):
            nonempty[j].update(i for i, s in enumerate(sect) if s)
    for sections in unfiltered:
        r = [[] for i in range(3)]
        for i, sect in enumerate(sections):
            for j, s in enumerate(sect):
                if j in nonempty[i]:
                    r[i].append(s)
        yield r

for sections in nonempty_rows():
    print ' '.join(','.join(map(str, s)) for s in sections)
