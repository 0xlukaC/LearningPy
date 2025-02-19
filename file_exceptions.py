#!/usr/bin/python

with open("data.txt", "w") as f:
    f.write("content\n")

try:
    with open("data.txt", "r") as f:
        print(f.read())
        print("number of lines", len(f.readlines()))
except fileNotFoundError as e:
    print("error ", e)


try:
    with open("user_output.txt", "w") as f:
        f.write(input("input stuff "))
except as e :
    print(e)

try:
    with open("data.txt", "r") as f:
        with open("output.txt", "w") as o:
            o.write(f.read())
except as e:
    print("error: " e)





lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    with open("user_output.txt", "w") as f:
        f.write(line)

print(lines)

