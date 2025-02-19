# Time Complexity:
# - O(NK log(NK)) where N is the number of accounts and K is the average number of emails per account
# - Union-find operations take O(NK × α(N)) where α is the inverse Ackermann function
# - Sorting emails for each merged account takes O(K log K) for each unique account
# - Overall dominated by the sorting step

# Space Complexity:
# - O(NK) for storing the ownership map and the merged accounts
# - O(N) for the DisjointSet data structure

# INTUITION:
# We need to merge accounts that share common emails. This is a perfect use case for Union-Find
# as we're dealing with connecting components based on shared elements.
#
# Example:
# accounts = [
#   ["John", "a@mail.com", "b@mail.com"],
#   ["John", "b@mail.com", "c@mail.com"],
#   ["Mary", "d@mail.com"]
# ]
#
# When we process "b@mail.com" in the second account, we find it's already owned by account 0,
# so we merge accounts 0 and 1. This gives us the connected component {a@mail.com, b@mail.com, c@mail.com}
# under John's name.

# ALGO:
# 1. Initialize DisjointSet and ownership map
# 2. First pass: Process each account
#    - For each email in account:
#      * If email exists in ownership map, union current account with existing owner
#      * Add/update email ownership
# 3. Second pass: Build merged accounts
#    - Group emails by their parent account (after union operations)
#    - Sort emails within each group
# 4. Return list of merged accounts with names

class DisjointSet:
   def __init__(self, n):
       self.parent = list(range(n+1))  # Parent array for union-find
   
   def findParent(self, node):
       # Path compression
       if self.parent[node] != node:
           self.parent[node] = self.findParent(self.parent[node])
       return self.parent[node]
       
   def union(self, i, j):
       parentOfI = self.findParent(i)
       parentOfJ = self.findParent(j)
       
       # If already in same component, return
       if parentOfI == parentOfJ:
           return
           
       # Merge components
       self.parent[parentOfJ] = parentOfI


class Solution:
   def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
       # Initialize Union-Find data structure
       disjointSet = DisjointSet(len(accounts))
       
       # Map each email to its owner (account index)
       emailToOwner = {}
       
       # First pass: Process all accounts and emails
       for accountIdx, (_, *emails) in enumerate(accounts):
           for email in emails:
               if email in emailToOwner:
                   # If email exists, union current account with existing owner
                   disjointSet.union(accountIdx, emailToOwner[email])
               emailToOwner[email] = accountIdx
       
       # Second pass: Build merged accounts
       mergedAccounts = defaultdict(list)
       for email, owner in emailToOwner.items():
           # Group emails by parent account
           parentOwner = disjointSet.findParent(owner)
           mergedAccounts[parentOwner].append(email)
       
       # Construct final result
       # Add name and sort emails for each merged account
       return [[accounts[accountIdx][0]] + sorted(emails) 
               for accountIdx, emails in mergedAccounts.items()]
