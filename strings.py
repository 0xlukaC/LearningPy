#!/usr/bin/python

name = "luka"
print(name[0])
print(name[-1])
print(name[1:3])

sentence = "Python is bad"
sentence.replace("bad", "really bad")

words = ["Mick’s","Class","is" ,"fun!"]
print(" ".join(words))

email = "george@japanmarshalls.com"
email = email.split("@")
print(email[0], email[1])

vowels = ['a', 'e', 'i', 'o', 'u']
def piglatin(word):
    if word[0] in vowels:
        return word + "yay"
    elif word[0:1] not in vowels and word[0:1].isalpha():
        replaced = word[0:1]
        word = word.replace(word[0:1])
        return word[1:] + replaced + "ay"
    elif word[0] not in vowels and word[0].isalpha():
        return word + "ay"
print(piglatin("eshay"))

