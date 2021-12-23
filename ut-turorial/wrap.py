import textwrap

def wrap(string, max_width):
    chunks, steps = len(string), max_width
    return [ (i, string[i:i+steps]) for i in range(0, chunks, steps) ]

if __name__ == '__main__':
    #string, max_width = input(), int(input())
    string, max_width = "ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4
    print(*wrap(string, max_width))