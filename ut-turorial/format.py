def print_formatted(number):
    # your code goes here
    padding = len(format(number, 'b'))
    print(padding)

    for i in range(1, number+1):
        print(format(i, 'd').rjust(padding), format(i, 'o').rjust(padding), format(i, 'x').capitalize().rjust(padding), format(i, 'b').rjust(padding))

if __name__ == '__main__':
    #n = int(input())
    n = 17
    print_formatted(n)