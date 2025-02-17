#!/usr/bin/python3
import random

Matrix = [[0 for _ in range(5)] for _ in range(5)]
print(Matrix)

for i in range(len(Matrix)):
    for j in range(len(Matrix[i])):
        if i == j:
            Matrix[i][j] = 1
print(Matrix)


Mat3 = [[1 + int(random.random() * (10 - 1)) for _ in range(3)] for _ in range(3)]
print(Mat3)

for i in range(len(Mat3)):
    for j in range(i + 1, len(Mat3)):
        Mat3[i][j], Mat3[j][i] = Mat3[j][i], Mat3[i][j]
print(Mat3)


books = [
    {"book_title": "The Road", "author": "Cormac McCarthy", "publication_year": 2006},
    {
        "book_title": "Harry Potter and the Goblet of Fire",
        "author": "J.K. Rowling",
        "publication_year": 2000,
    },
    {
        "book_title": "The Night Circus",
        "author": "Erin Morgenstern",
        "publication_year": 2011,
    },
    {
        "book_title": "The Da Vinci Code",
        "author": "Dan Brown",
        "publication_year": 2003,
    },
    {"book_title": "Life of Pi", "author": "Yann Martel", "publication_year": 2001},
]


for book in books:
    if book["publication_year"] > 2000:
        print(book["book_title"])
