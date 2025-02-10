#!/usr/bin/python3


def compression(input):
    newstring = ""
    past = input[0]
    count = 1

    for i in range(1, len(input)):
        if input[i] == past:
            count += 1
        else:
            newstring += past
            if count > 1:
                newstring += str(count)
            past = input[i]
            count = 1

    newstring += past + (str(count) if count > 1 else "")
    if len(input) > len(newstring):
        return newstring


print(compression("hellooo"))
