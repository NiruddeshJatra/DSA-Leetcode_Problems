# Time Complexity: O(n), where n is the number of gas stations. We traverse the `gas` and `cost` lists in one pass.
# Space Complexity: O(1), as we only use a constant amount of extra space for variables like `remainingGas` and `ans`.

# INTUITION:
# The problem involves determining the starting gas station from which a car can complete a circuit of stations 
# if it has enough gas to cover the costs. If the total gas available is less than the total cost, it's impossible 
# to complete the circuit, and we return -1.
# 
# **Key Insight**: If the sum of gas is greater than or equal to the sum of the cost, then a solution exists. 
# The challenge is to determine the starting point.
# 
# **Greedy Approach**: We can traverse the stations and track the amount of remaining gas at each step. If at any point 
# the remaining gas becomes insufficient to move to the next station, we reset the starting point to the next station. 
# By the time we complete one loop, if a valid solution exists, the last reset station will be the answer.

# ALGO:
# 1. **Check Feasibility**: 
#    - If the total gas is less than the total cost, return -1 since it's impossible to complete the circuit.
# 2. **Traverse the Stations**:
#    - Initialize the starting point (`ans`) and the `remainingGas` to the gas available at the first station.
#    - Traverse through the stations.
#    - For each station, check if the remaining gas is less than the cost to move to the next station.
#        - If it is, reset the starting point to the current station and reset the remaining gas.
#        - Otherwise, continue accumulating the remaining gas.
# 3. **Return the Starting Station**:
#    - The last reset starting station (`ans`) is returned as the result.

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Step 1: Check if completing the circuit is feasible
        if sum(gas) < sum(cost):
            return -1
        
        # Step 2: Initialize variables for the greedy approach
        ans = 0
        remainingGas = gas[0]
        
        # Step 3: Traverse the gas stations
        for i in range(1, len(gas)):
            # Step 4: If we can't move to the next station, reset the starting point
            if remainingGas < cost[i - 1]:
                ans = i
                remainingGas = gas[i]  # Reset the gas to the current station's gas
            else:
                remainingGas += (gas[i] - cost[i - 1])  # Continue accumulating the remaining gas
        
        # Step 5: Return the starting station that allows completing the circuit
        return ans
