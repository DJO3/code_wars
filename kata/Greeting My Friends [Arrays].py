"""
We give you an Array of friend's list.

Write a function called greeting_for_all_friends that takes one argument, friends.

This method takes an array of friends name and return a greeting messages Array.

Message sample: for the friend "Bilal" we get "Hello, Bilal!"

Rules:

If the argument is null, the method should return null
If the argument is an empty array, the method should return null
If the argument is a valide array of strings, the method should return a hello message for every array entry
"""

import sys

def greeting_for_all_friends(friends):
    if friends != None and friends:
        greeting = ["Hello, {}!".format(friend) for friend in friends]
        return greeting

if __name__ == "__main__":
    f = sys.argv[1:]
    print(greeting_for_all_friends(f))

# print(greeting_for_all_friends(["Bob"]))
