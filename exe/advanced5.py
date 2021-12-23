from functools import reduce
from random import randint

data = range(100)

result = [i for i in data if i % 2 == 0]
#print(result)

result = reduce(lambda a,b: a+b, filter(lambda x: x % 2 == 0, data))
print(result)

d = { x: randint(50, 100) for x in range(1, 22) }
result = {k: v for k,v in d.items() if v > 80}
print(result)