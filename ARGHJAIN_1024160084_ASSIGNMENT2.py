# 1. Take your roll number. Extract its individual digits, and multiply each digit by 10 to form your list L (10
# numbers in list now).

roll_no = 1024160084
L = [int(digit) * 10 for digit in str(roll_no)]

# i. Print L
print("L = ",L)

# ii. Add two numbers of your choice to L — one using append() and one using insert() at a specific position.
# Print L after each and explain in a comment what changed.
L.append(25) # add 25 at the end of the list
print("L = ",L)
L.insert(3, 50) # add 50 at index 3
print("L = ",L)

# iii. Remove two elements from L — one using remove() and one using pop(). Print L after each.
L.remove(25) # remove 25 from the list
print("L = ",L)
L.pop(2) # remove the element at index 2
print("L = ",L)

# iv. Sort L in ascending order using sort(), then descending order using sort(reverse=True). Print both.
L.sort() # sort the list
print("L = ",L)
L.sort(reverse=True) # sort the list in descending order
print("L = ",L)

# v. Use slicing to print the first three elements and the last three elements of L in a single line each.
print("First three elements:", L[:3])
print("Last three elements:", L[-3:])

# vi. Use list comprehension to create a new list containing only the elements of L that are greater than the
#average of L.
average = sum(L) / len(L) # calculate the average of the list
print("Average of the list:", average)

New_L = [x for x in L if x > average] # create a new list with elements greater than the average
print("New list with elements greater than the average:", New_L)


# 2. Create a tuple named scores containing 8 marks: use the first 8 values from your list L in Q1.
scores = (10, 0, 20, 40, 10, 60, 0, 10)

# i. Find the highest score and its index in the tuple, and the lowest score and how many times it appears.

highest = max(scores)
highest_index = scores.index(highest)

lowest = min(scores)
lowest_count = scores.count(lowest)

print("Highest score:", highest)
print("Index of highest score:", highest_index)
print("Lowest score:", lowest)
print("Lowest score appears:", lowest_count, "times")

# ii. Reverse the tuple and return the result as a list (tuples themselves cannot be reversed in place —
# explain why in a one-line comment, referring to tuple immutability).

reversed_scores = list(scores[::-1])

print("Reversed tuple as list:", reversed_scores)

# Tuples cannot be reversed in place because tuples are immutable.

# iii. Ask the user to input a score. Print its first occurrence index if present in the tuple, or a not present
# message if not.

score = int(input("Enter a score: "))

if score in scores:
    print("First occurrence index:", scores.index(score))
else:
    print("Score not present in the tuple")

# iv. Attempt to change one element of the tuple directly (e.g., scores[0] = 100). Run it, capture the error
# Python raises, and explain in one line why this happens and how it differs from a list.

##  This will cause an error since tuples are immutable
##  scores[0] = 100

# v. Unpack the tuple into a first score, a second score, and all remaining scores using the * operator in a
# single line of unpacking.

first_score, second_score, *remaining_scores = scores

print("First score:", first_score)
print("Second score:", second_score)
print("Remaining scores:", remaining_scores)


# 3. Set the random seed to your own roll number using random.seed(your_roll_number) before generating
# your numbers — this keeps your list random-looking but reproducible and unique to you (a different seed
# produces a different list, so this cannot be copied from a classmate).

import random

random.seed(1024160084)


# i. Generate a list of 100 random numbers between 100 and 900 (inclusive).
numbers = [random.randint(100, 900) for _ in range(100)]

print("Random numbers:")
print(numbers)

# ii. Count and print all odd numbers in the list.
odd_numbers = [x for x in numbers if x % 2 != 0]

print("Odd numbers:", odd_numbers)
print("Number of odd numbers:", len(odd_numbers))

# iii. Count and print all even numbers in the list.
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)
print("Number of even numbers:", len(even_numbers))

# iv. Count and print all prime numbers in the list, and additionally build the actual list of prime numbers
# found using list comprehension.
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

prime_numbers = [x for x in numbers if is_prime(x)]

print("Prime numbers:", prime_numbers)
print("Number of prime numbers:", len(prime_numbers))

# v. Print the number that occurs most frequently in your list, and how many times it occurs
most_frequent = max(numbers, key=numbers.count)
frequency = numbers.count(most_frequent)

print("Most frequent number:", most_frequent)
print("It occurs:", frequency, "times")

# 5. Consider the following dictionary:

# my_dict = {
#  "name": "<your name>",
#  "roll_no": "<your roll number>",
#  "branch": "<your branch>",
#  "age": <your age>,
#  "city": "<your home city>"
# }
my_dict = {
    "name": "Argh Jain",
    "roll_no": "1024160084",
    "branch": "COSE",
    "age": 20,
    "city": "Ajmer"
}

print(my_dict)

# i. Rename the key “city” to “location” without changing its value (do not just recreate the dictionary by
# hand — use pop() or dictionary comprehension so the code would work for any dictionary).
my_dict["location"] = my_dict.pop("city")

print(my_dict)

# ii. Add a new key “cgpa” with your CGPA as its value.
my_dict["cgpa"] = 8.5

print(my_dict)

# iii. Update the value of “age” by increasing it by 1.
my_dict["age"] = my_dict["age"] + 1

print(my_dict)

# iv. Delete the “branch” key using two different methods in two separate copies of the dictionary: once
# with pop() and once with the del keyword. Explain in one line how pop() differs from del (hint: what
# does each return?).
dict1 = my_dict.copy()
dict2 = my_dict.copy()

removed_branch = dict1.pop("branch")

print("After pop():", dict1)
print("Removed value:", removed_branch)

del dict2["branch"]

print("After del:", dict2)

# pop() removes the key and returns its value, while del removes the key without returning its value.
# v. Iterate over your dictionary using .items() and print each key-value pair as “key → value”.

# vi. Before accessing a key called “email” (which doesn't exist in your dictionary), check for its existence
# using the in keyword and print a safe fallback message instead of letting the program crash.

# vii. Create a second dictionary friend_dict with the same 5 original keys but a friend's (fictional) details.
# Merge it with your own using the {**dict1, **dict2} syntax, and explain in one line which values “win”
# when both dictionaries share a key.
friend_dict = {
    "name": "Moksh",
    "roll_no": "1024160101",
    "branch": "CSE",
    "age": 20,
    "city": "Haryana"
}

merged_dict = {**my_dict, **friend_dict}

print("Merged dictionary:", merged_dict)

# viii. Use dictionary comprehension to create a new dictionary containing only the key-value pairs from your
# original dictionary where the value is a string.
string_values = {
    key: value for key, value in my_dict.items()
    if isinstance(value, str)
}

print("String values:", string_values)
