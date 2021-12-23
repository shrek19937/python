apples = [ 1, 3, 7]
oranges = [11, 17, 19]
d = (10, 7)
af = [ -5, 3, 6]
of = [ -3, 7, 3 ]

apple_pos = [ a[0] + a[1] for a in zip(apples, af) ]
#print(list(apple_pos))

orange_pos = [ a[0] + a[1] for a in zip(oranges, of) ]
#print(list(orange_pos))

a = [ x for x in apple_pos if x < d[0] + d[1] and x > d[0] - d[1]]
print(f"apples within range, {a}")

o = [ x for x in orange_pos if x < d[0] + d[1] and x > d[0] - d[1]]
print(f"orange within range, {o}")