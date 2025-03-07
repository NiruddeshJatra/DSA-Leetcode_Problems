# Time Complexity:
# - insert(): O(1) average case for set operations
# - remove(): O(1) average case for set operations
# - getRandom(): O(n) where n is the number of elements, due to conversion from set to list
#
# Overall, insert and remove are efficient, but getRandom suffers due to set-to-list conversion.

# Space Complexity:
# - O(n) where n is the number of unique elements stored in the set

# INTUITION:
# This problem requires implementing a data structure that supports insertion, deletion, and
# random access, all in constant time. Using a Python set gives us O(1) insertion and deletion,
# but getting a random element requires converting the set to a list, which takes O(n) time.
#
# A more efficient approach would be to use both a list and a dictionary (hash map):
# - The list allows O(1) random access by index
# - The dictionary maps values to their indices in the list for O(1) lookups
# - For removal, we can swap the element to be removed with the last element in the list,
#   then remove the last element (which is now O(1))
#
# However, the current implementation uses a simpler approach with just a set, sacrificing
# performance on getRandom() for code simplicity.

# ALGO:
# The current implementation uses Python's built-in set:
# 1. insert(): Add the value to the set if it doesn't exist
# 2. remove(): Remove the value from the set if it exists
# 3. getRandom(): Convert the set to a list and use random.choice()
#
# While functional, the getRandom() method is not O(1) as required by the problem.

class RandomizedSet:

   def __init__(self):
       """
       Initialize your data structure here.
       """
       self.values = set()  # Store unique values

   def insert(self, val: int) -> bool:
       """
       Inserts a value to the set.
       Returns true if the set did not already contain the specified element.
       """
       if val in self.values:
           return False
       
       self.values.add(val)
       return True

   def remove(self, val: int) -> bool:
       """
       Removes a value from the set.
       Returns true if the set contained the specified element.
       """
       if val in self.values:
           self.values.remove(val)
           return True
       
       return False

   def getRandom(self) -> int:
       """
       Get a random element from the set.
       Each element must have the same probability of being returned.
       """
       import random
       return random.choice(list(self.values))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
