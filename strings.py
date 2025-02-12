#!/usr/bin/python3

name = "luka"
print(name[0])
print(name[-1])
print(name[1:3])

sentence = "Python is bad"
sentence.replace("bad", "really bad")

words = ["Mick’s", "Class", "is", "fun!"]
print(" ".join(words))

email = "george@japanmarshalls.com"
email = email.split("@")
print(email[0], email[1])


# def pigsentence(word):
#     vowels = ["a", "e", "i", "o", "u"]
#
#     def piglatin(word):
#         if word[0] in vowels:
#             return word + "yay"
#         elif word[0:1] not in vowels and word[0:1].isalpha():
#             replaced = word[0:1]
#             word = word.replace(word[0:1])
#             return word[1:] + replaced + "ay"
#         elif word[0] not in vowels and word[0].isalpha():
#             return word + "ay"
#
#     for i in word.split():
#         piglatin(i)


def pigsentence(sentence):
    vowels = {"a", "e", "i", "o", "u"}  # Using a set for faster lookup

    def piglatin(word):
        if word[0] in vowels:
            return word + "yay"
        else:
            return word[1:] + word[0] + "ay"  # Move first letter to the end

    return " ".join(piglatin(word) for word in sentence.split())


print(pigsentence("eshay"))  # "eshayyay"
print(pigsentence("hello world"))  # "ellohay orldway"

print(pigsentence("eshay"))
