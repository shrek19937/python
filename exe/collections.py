#python class
#file handling
#exception handling
#list of python collection class
#basic ops, CRUD
#list comprehension
#re
from pathlib import Path

#python class
class auser:
    def __init__(self, id, fname, lname):
        self.id    = id
        self.fname = fname
        self.lname = lname
    
    def __str__(self):
        return f"{self.id}, {self.fname}, {self.lname}"

auser = auser(1, "michael", "wu")
print(auser)

#file handling
def print_file(fname):
    with open(fname, "r") as f:
        for line in f:
            print(f"{line}", end = "")
    print()
print_file(f"{str(Path.home())}/python-code/exe/read-stdin.py")

#collection data types
#  list, tuple, set, dictionary. stack could be implemented using list, see below
#basic ops, CRUD
list1 = [1, 2, 3]
list2 = [3, 4, 5]
aset  = set()
aset.add(1); aset.add(5), aset.add("A")
adict = {"a":1, "b":2, "c":3}
adict.update({"d":4})  #dict add/update
adict["e"] = 5         #dict add
print(aset)
print(adict)
atuple = ("fname", "shrek")
print(atuple)

#list comprehension
common  = [ i for i in list1 if i in list2 ]; print(common)   #find common list
common2 = [ a for a in list2 if a in aset ];  print(common2)
#collection - stack implemented using list
#exception handling

#stack to validate match parameters
openers = { '{':'}', '[':']', '(':')' }
closers = { '}', ']', ')' }

def is_it_a_match(s):
    symbols = []

    for c in s:
        try:
            #print(c, len(symbols))

            if c in openers:
                symbols.append(c)
            elif c in closers:
                if len(symbols) == 0:
                    return False

                oc = symbols.pop()
                if openers[oc] != c:
                    return False
        except Exception as e:  #some char that's neither an opener, nor a closer
            print(f"caught exception {e}")
            continue #ignore it
    
    if len(symbols) == 0:
        return True

    return False

if __name__ == "__main__":
    print(is_it_a_match("{[] ()}"))
    print(is_it_a_match("{[]()}]"))