print("hello min stack")

class minstatck:
    min = None
    container = []

    def pop(self):
        if (len(self.container) == 0):
            return None

        r = self.container[-1]
        del (self.container[-1])
        self.min = min(self.container)
        return r

    def push(self, i):
        if self.min == None or i < self.min:
            self.min = i

        self.container.append(i)

    def mv(self):
        return self.min

ms = minstatck()
print(type(ms))
ms.push(1)
ms.push(2)    
ms.push(3) 
print(ms.mv())

print(ms.pop())
print(ms.pop())


        

