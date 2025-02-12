#!usr/bin/python

# stacks - LIFO
# interface: O(1)
## pop
## push
## peak
## is_empty()

# best to implement with a list


# queues FIFO

# interface: O(1)
## enqueue
## dequeue
## peak
## is_empty()


# collections (module) provides a queue class

from collections import deque

queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)

print(queue.popleft()) # left because theres a pointer on the left (returns 10)
#print(queue.remove[1])



# tuples - group of things - ordered - immutable

numbers = (3, 4)
compl_num = (2, 7)
print(numbers) # 3, 4




# Dictionaries - O(1) - unordered collection of key-value pairs - hash map

## get(key)
## keys() -> get all keys
## values() -> get all the values
## items() -> get all pairs

capitals = {
        "Germany": "Berlin",
        "Canada" : "Ottowa",
        "England" : "London",
        "Bhutan" : "Thimphu",
        "Thailand", "Bangkok",
        "Australia", "Sydney"
    }

capitals["Australia"] = "canberra"
print(capitals["Canada"])
# print(capitals["japan"]) # error
capitals["Japan"] = "Tokyo"

for key, value in capitals.items():
    print(key)
    print(value)
    if value == "Canberra"
        print(key)





# Sets - unordered collection - no duplicates
## union
## Intersection
## set difference
## {} or set()

s = {"apple", "banana", "cherry", "pear", "durian"} # not a dictionary because there are no : 
t = {"mango", "apple", "grape"}
print(s & t) # subset
print(s | t) # union - everything without duplicates









