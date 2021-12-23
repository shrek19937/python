myset = set([1,2,3,4,6, 5])

print(myset)

print(1 in myset)
print(5 in myset)

sum = 0
for i in myset:
    sum += i

total = 0
for i in range(1, 7):
    total +=i

print(total, sum, total - sum)

set2 = { 1, 2, 3, 2 }
set2.add(7)
print(set2)