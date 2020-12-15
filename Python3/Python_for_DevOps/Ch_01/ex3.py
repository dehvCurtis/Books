# Python for DevOps
# Chapter 1

# Write a list comprehension that results in a list of every letter in the word smogtether capitalized.

string = 'smogtether'

list_comprehension = [letter.upper()  for letter in string]

print(list_comprehension)