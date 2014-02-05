def db(path):
    with open(path, 'r') as f:
        for line in f:
            yield line.split('\t')

HIERARCHY = dict([(a[1], [a[0]]) for a in db('hierarchy.txt')])


def ancestors(child):
    if child not in HIERARCHY:
        return []
    parents = HIERARCHY[child]
    grand_parents = ancestors(parents[-1])
    if grand_parents == []:
        return parents
    parents = parents + grand_parents
    return parents


def reverse_ancestor(child):
    a = ancestors(child)
    a.reverse()
    return a

k = HIERARCHY.keys()[0]
print reverse_ancestor(k)
