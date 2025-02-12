#!/usr/bin/python3


def is_balanced(input):
    counter = 0
    while input:
        char = input.pop()
        if char == "(":
            counter += 1
        elif char == ")":
            counter -= 1
    if not counter:
        return True
    return False


def freqChar(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return max(freq, key=lambda k: freq[k])


string = "abcd(a(a)abdcd"
string = [i for i in string]
print(string)
print(is_balanced(string))
print(freqChar("hello world"))
