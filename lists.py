#!/usr/bin/python3
mylist = ["h", "e", "l", 2, "o"]
print(mylist[len(mylist) - 1])


oneto20 = [i + 1 for i in range(20)]

ten = [i + 1 for i in range(10)]
ten.remove(2)
ten.pop(5)  # pop is indexed, remove is first occurance

squares = [i**2 for i in range(1, 51) if i**2 > 20]
print(squares)

Nested = [
    [79, 4, 36],
    [67, 98, 44, 12, 26],
    [50],
    [32, 96, 15, 24, 46],
    [5, 74, 99, 50, 42, 34, 28],
    [37],
    [72, 60, 26],
    [79, 3, 25, 95, 19, 17],
    [98, 19],
    [99, 77, 94, 40, 44, 76, 17, 72, 56],
]

newList = [len(i) for i in Nested]

print(newList)
