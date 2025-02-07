#!/usr/bin/python3

# check if a string is entirely  made up of unique characters
# return a bool


# o(n) since set is a hashmap
def unique(string):
    checked = set()
    for i in string:
        if i in checked:
            return False
        checked.add(i)
    return True


print(unique("abcdf"))  # true
print(unique("senselessness"))  # false
print(unique(""))  # true
