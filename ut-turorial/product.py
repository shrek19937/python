l1 = [1,2,3]
l2 = [5,6,7]

p = [ (a, b, a+b) for a in l1 for b in l2 if (a+b) > 8 ] + [(-1, -1, -1)]

print(type(p), p, max(p))