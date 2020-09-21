"""Introduction to the most common collections methods"""


from collections import namedtuple, defaultdict, Counter, deque
import timeit
import random


# 1. namedtuple to make code more readable
normal_tuple = ('bob', 'coder')
print(f'{normal_tuple[0]} is a {normal_tuple[1]}')

User = namedtuple('User', 'name role')
new_tuple = User(name='bob', role='coder')

print(f'{new_tuple.name} is a {new_tuple.role}')


# 2. defaultdict is important while building nested DS
#      and when we do not have the information of key
normal_dict = {"bob": "coder"}
print(normal_dict["bob"])
# this will fail as the key julian is not in the dict
# print(normal_dict["julian"])

print(normal_dict.get("bob"))

# this will not fail but will give the value None
print(normal_dict.get("julian"))

# build a dictionary from this list of tuples
challenges_done = [('tom', 10), ('dick', 7), ('harry', 5),
                   ('tom', 11), ('dick', 8), ('harry', 6)]

print(challenges_done)

# Using normal dictionary in 2 ways
challenges = {}

# This will give keyerror
# for name, challenge in challenges_done:
#     challenges[name].append(challenge)

# This will overwrite the older values
# for name, challenge in challenges_done:
#     challenges[name] = challenge
# print(challenges)

# Using defaultdict
challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)

print(challenges)


# 3. Counter to count the most common words
words = "hello hello hi hi hello hi my name is hello kitty hi oh no hi! Bye good bye".split()
print(Counter(words).most_common(2))


# 4. deque is a combination of stacks and queues
# this can be used as a replacement for lists
# lists are the most useful data structure in Python
# but if there needs a lot of changes in the positions
# then it can become very slow and that's when deque helps

lst = list(range(10000000))
deq = deque(range(10000000))


def insert_and_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)

# On using timeit module, the difference between
# list and deque is of the order of 10^3
# deque being the faster of the two
