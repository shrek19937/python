for i in range(0, 100):
    if (0 == i % 2 and 0 == i % 3):
        print("buzz fuzz")
        continue

    if (0 == i % 2):
        print("buzz")
        continue

    if (0 == i % 3):
        print("fuzz")
        continue

    print(i)