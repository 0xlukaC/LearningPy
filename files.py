#!/usr/bin/python

"""
Read and write in python

use open() function, function to read write files
the mode 'char'
r - read
w - write - overwrites
a - append - adds to an existing file

once you have opened the file you can use read() and write()
read: read the entire file - returns a string
readline: read one line at a time
readlines: returns a list of all the lines


'with' keyword is used for safety, it closes the file and recycles any resources involved once you are done You can use the file.close()
to close files explicitly

"""

with open("example.txt", "w") as f:
    f.write("Hello, file\n")

with open("example.txt", "r") as f:
    s = f.read(-1)  # number of bytes to read
    print(s)


"""
    exeptions:
    Also use else/finally keywords for more control
"""

try:
    with open("non-existent.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError as e:
    print("err file not found", e)

except PermissionError:
    print("no permission")
except:
    print("some kind of error")
else:  # executees if everything went well
    print("no exceptions")
finally:  # executes always regardless of error or no error
    print("done with finally block")
