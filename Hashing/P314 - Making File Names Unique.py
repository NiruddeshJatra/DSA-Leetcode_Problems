# Time Complexity:
# - O(N * K), where N is length of names array
# - K is max number of times we need to try different suffixes
# - In worst case, might need to try many suffixes for each name

# Space Complexity:
# - O(N) to store used names in dictionary
# - Also O(N) for returning list of modified names

# INTUITION:
# Keep track of used names and their highest suffix number.
# When collision occurs, try incrementing suffix until finding
# unused name. Need to track both base names and modified names
# to handle cases like ["name","name(1)","name","name(1)"]

# ALGO:
# 1. Create dictionary to track used names
# 2. For each name:
#    - Try using name as is
#    - If taken, get last used suffix k
#    - Try name(k+1) until finding unused version
#    - Update suffix counter for base name
#    - Add final name to used set
# 3. Return list of all used names

class Solution:
   def getFolderNames(self, names: List[str]) -> List[str]:
       usedNames = {}  # Maps names to their highest used suffix
       
       for originalName in names:
           modifiedName = originalName
           
           if modifiedName in usedNames:
               suffixCount = usedNames[originalName]
               
               # Try increasing suffixes until finding unused name
               while modifiedName in usedNames:
                   suffixCount += 1
                   modifiedName = f'{originalName}({suffixCount})'
               
               # Update suffix counter for original name
               usedNames[originalName] = suffixCount
               
           # Mark new name as used with initial suffix 0
           usedNames[modifiedName] = 0
           
       return list(usedNames.keys())
