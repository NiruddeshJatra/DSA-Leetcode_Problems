# Time Complexity:
# - O(N), where N is the length of the input path string
# - split() operation is O(N)
# - Each directory is processed once
# - join() operation is O(N)

# Space Complexity:
# - O(N) to store the canonical path components
# - In worst case, all directories are valid and stored in answer array
# - Additional O(N) for string split operation

# INTUITION:
# Unix paths have special characters ('.','..','/') that affect navigation.
# Using a stack (array) for path components is ideal because:
# 1. '..' removes last directory (pop from stack)
# 2. '.' and empty strings can be ignored
# 3. Valid directories are simply added
# 4. Final path is stack contents joined with '/'
# 5. Stack naturally handles nested paths

# ALGO:
# 1. Split path by '/' to get directories
# 2. Process each directory:
#    - If '..': pop last directory if stack not empty
#    - If '.' or empty: skip
#    - Otherwise: add directory to stack
# 3. Join stack contents with '/' and add leading '/'

class Solution:
   def simplifyPath(self, path: str) -> str:
       # Stack to store valid directory names
       pathComponents = []
       
       # Split path by '/' and process each component
       for directory in path.split('/'):
           # Handle parent directory navigation
           if directory == '..':
               if pathComponents:
                   pathComponents.pop()
           # Add valid directory names (ignore '.' and empty strings)
           elif directory and directory != '.':
               pathComponents.append(directory)
       
       # Construct canonical path with leading '/'
       return '/' + '/'.join(pathComponents)
