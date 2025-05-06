#!usr/bin/python

"""
Iterators:
    abstraction which represents a data stream implements two methods iter() and next()

    certain data structures are iterable (if you can loop though them)
    On these data strctures we can call iter() to generate an iterator that points to them
"""

characters = ["mario", "luigi", "wario", "toad", "yoshi"]

characters_iter = iter(characters)
print(characters_iter)
print(next(characters_iter))


# Custom Iterators
# Generators

# Lazy Execution - only execute as you need the result
# Eager execution - execute everything upfront


# Generator Function
def count_up_to(n):
    count = 0
    # imagine if this was computationally intensive
    while count < n:
        yield count
        # print(count)
        count += 1


gen = count_up_to(5)

print(next(gen))
print(next(gen))
gen2 = count_up_to(8)
print(next(gen2))


# Generator Expression - syntax sugar

gen_exp = (x**2 for x in range(5))

for v in gen_exp:
    print(v)
