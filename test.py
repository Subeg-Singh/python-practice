def rotator():
    array = [1, 2, 3, 4, 5]

    k = int(input("Enter number of rotations: "))

    for _ in range(k):
        array.insert(0, array[-1])
        array.pop()

    print(array)

rotator()