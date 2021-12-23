is_male = True

if is_male:
    print("this is a male")
else:
    print("this is NOT a male")


def max(a, b, c):
    bigger = a
    if (a <= b):
        bigger = b
    
    if (bigger <= c):
        bigger = c

    return bigger

print(max(1,2, 4) )