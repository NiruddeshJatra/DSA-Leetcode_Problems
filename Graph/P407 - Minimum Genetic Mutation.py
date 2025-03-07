# Time Complexity:
# - O(N * L), where N is the number of genes in the bank and L is the length of each gene (8 in this problem).
# - For each gene in the queue, we check all genes in the bank, comparing each character.

# Space Complexity:
# - O(N) for the queue and visited set, where N is the number of genes in the bank.
# - In the worst case, all genes in the bank could be added to the queue and visited set.

# INTUITION:
# This problem asks for the minimum number of mutations needed to transform the start gene to the end gene,
# where each mutation changes exactly one character and must result in a valid gene from the bank.
#
# This is a classic shortest path problem, where:
# - Nodes are valid gene strings
# - Edges connect genes that differ by exactly one character
# - We want to find the shortest path from the start gene to the end gene
#
# BFS is ideal for finding the shortest path in an unweighted graph. We can model the problem as a graph
# and use BFS to find the minimum number of mutations (edges) needed to reach the end gene.
#
# For example, with start="AACCGGTT", end="AAACGGTA", and bank=["AACCGGTA","AACCGCTA","AAACGGTA"]:
# - We start at "AACCGGTT"
# - We can mutate to "AACCGGTA" (1 mutation)
# - We can mutate to "AACCGCTA" (1 mutation from "AACCGGTA")
# - We can mutate to "AAACGGTA" (1 mutation from "AACCGCTA")
# So the minimum number of mutations is 3.

# ALGO:
# 1. Define a helper function to check if two genes are neighbors (differ by exactly one character).
# 2. Use BFS to find the shortest path:
#    a. Initialize a queue with the start gene and a mutation count of 0.
#    b. Initialize a visited set to prevent revisiting genes.
#    c. For each gene in the queue:
#       i. If it's the end gene, return the mutation count.
#       ii. Otherwise, check all genes in the bank that differ by exactly one character.
#       iii. Add valid unvisited neighbors to the queue with an increased mutation count.
# 3. If BFS completes without reaching the end gene, return -1 (impossible).

class Solution:
   def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
       """
       Find the minimum number of mutations needed to mutate from startGene to endGene.
       Each mutation can change exactly one character in the gene string.
       Only mutations that result in a string in the bank are valid.
       
       Args:
           startGene: String representing the starting gene
           endGene: String representing the target gene
           bank: List of valid gene strings
       
       Returns:
           Minimum number of mutations or -1 if impossible
       """
       # Helper function to check if two genes differ by exactly one character
       def isDifferentByOne(geneA, geneB):
           differences = 0
           for i in range(len(geneA)):
               if geneA[i] != geneB[i]:
                   differences += 1
               # Early termination if we found more than one difference
               if differences > 1:
                   return False
           return differences == 1
       
       # If endGene is not in the bank, it's impossible to reach
       if endGene not in bank:
           return -1
       
       # Initialize queue for BFS with [current gene, mutation count]
       queue = deque([(startGene, 0)])
       # Track visited genes to avoid cycles
       visitedGenes = {startGene}
       
       # BFS to find shortest path
       while queue:
           currentGene, mutationCount = queue.popleft()
           
           # Check if we've reached the target
           if currentGene == endGene:
               return mutationCount
           
           # Try all possible valid mutations
           for candidateGene in bank:
               # Check if the candidate is a valid next mutation (differs by exactly one character)
               # and hasn't been visited
               if isDifferentByOne(currentGene, candidateGene) and candidateGene not in visitedGenes:
                   visitedGenes.add(candidateGene)
                   queue.append((candidateGene, mutationCount + 1))
       
       # If we've exhausted all possibilities without finding endGene
       return -1
