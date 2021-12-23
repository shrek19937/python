li = [1,2,3]
print(li)

ln = ["kevin", "karen", 'Jim']
print(ln[1])

ln.append("Mike")
ln.extend(li)

print(ln)
print(type(ln))
print(len(ln))

coord = (1, 1)  #immutable
print(coord)

coord = (2,2)   # a new object
print(coord)


d = { 
    "jan": 1,
    "feb": 2
}

print(d["jan"])
print(d.get("jan", "one"))