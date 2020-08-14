import time
from stack import Stack
from singly_linked_list import *

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# O(n^2) quadratic runtime.
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

#---------------------------------

# O(c^n) - Exponential runtime
# Using linked lists we increased the runtime to around 56 seconds.
# create first linked list
# ll = LinkedList()
# for name in names_1:
#     ll.add_to_tail(name)

# # create second linked list
# ll2 = LinkedList()
# for name in names_2:
#     ll2.add_to_tail(name)

# # create function to compare linked lists
# while ll.size > 0:
#     string = ll.remove_tail()
#     if ll2.contains(string):
#         duplicates.append(string)

#---------------------------------

# O(c^n) - Exponential runtime
# Using stack we increased the runtime to around 20 seconds.
# stack = Stack()
# for name in names_1:
#     stack.push(name)

# while stack.size > 0:
#     check_name = stack.pop()
#     if check_name in names_2:
#         duplicates.append(check_name)


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# using built in python methods we decreased the runtime to around 1.9-2 seconds.
# O(nlogn) runtime:
# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)

# The above using list comprehension; doesn't change runtime but it looks cleaner
# duplicates = [name for name in names_1 if name in names_2]

# Our fastest runtime yet
# O(n)
# runs at less than 1 second.

start_time = time.time()

new_list = set(set(names_1) & set(names_2))
new_list = list(set(new_list))

for name in new_list:
    duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
