#!/usr/bin/python3
"""
• Write a Python program, observer.py, and demonstrate the following:
     ◦ Write a NewsAgency class, which models a news agency, which readers can subscribe to to receive updates
     ◦ Write a Subscriber class to model subscribers to the service
     ◦ The NewsAgency class should store a list of Subscriber objects and have public methods to ‘subscribe’, ‘unsubscribe’ and ‘publish’ updates to its ‘subscribers’

"""


class NewsAgency:
    def __init__(self):
        self.subscribers = []

    def addSubscriber(self):
        self.subscribers.append(
            [Subscriber(len(self.subscribers) + 1), len(self.subscribers) + 1]
        )

    def notifySubscribers(self, message):
        for i in self.subscribers:
            i[0].update(message)

    def removeSubscriber(self, number):
        for i in self.subscribers:
            if i[1] == number:
                self.subscribers.remove(i)


class Subscriber:
    def __init__(self, id):
        self.id = id
        self.__latestUpdate = ""

    def update(self, update):
        self.__latestUpdate = update

    def getLatest(self):
        return self.__latestUpdate
