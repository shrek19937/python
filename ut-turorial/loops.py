i = 0
while(i < 5):
    print(i)
    i = i + 2

    #if (i == 10):
    #   break
print()

for i in range(3, 7):
    print(i)
print()

li = [1,2,3]
for i in li:
    print(i)

l = []
for i in range(0, 100, 7):
    l.append(i)
print(l)

l = [ (i, "5x") if i % 5 == 0 else (i, ) for i in range(0, 100, 3)  ]
print(l)