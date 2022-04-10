#list of python collection class
#basic ops, CRUD
#list comprehension
#file handling
#exception handling
#re
#classes

list1 = [1, 2, 3]
list2 = [3, 4, 5]

#find common list
#common = [ i for i in list1 if i in list2 ]; print(common)

class auser:
    def __init__(self, id, fname, lname):
        self.id    = id
        self.fname = fname
        self.lname = lname
    
    def __str__(self):
        return f"{self.id}, {self.fname}, {self.lname}"

auser = auser(1, "michael", "wu")
print(auser)


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