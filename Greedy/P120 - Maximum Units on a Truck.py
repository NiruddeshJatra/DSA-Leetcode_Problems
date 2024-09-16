# Time Complexity: O(n log n), where n is the length of the `boxTypes` array. Sorting the `boxTypes` array based on the number of units per box takes O(n log n), and the following loop to select boxes runs in O(n).
# Space Complexity: O(1), since we only use a constant amount of extra space for variables `boxes` and `truckSize`.

# INTUITION:
# The goal is to maximize the number of units that can be loaded onto a truck. Each type of box contains a certain number of units, and we are given a maximum truck capacity in terms of the number of boxes it can carry. 
#
# **Key Insight**:
# - To maximize the total number of units, we should prioritize boxes that contain the most units. Thus, we first sort the box types based on the units per box in descending order, and then greedily fill the truck by choosing boxes with the highest units first.

# ALGO:
# 1. **Sort the `boxTypes` array**:
#    - Sort the `boxTypes` in descending order based on the number of units per box (`x[1]`).
# 2. **Initialize `boxes` to 0**:
#    - `boxes` will store the total number of units loaded onto the truck.
# 3. **Greedily load the truck**:
#    - Traverse each `boxType` in the sorted array. For each box type:
#       - If the remaining truck capacity (`truckSize`) is greater than or equal to the number of available boxes of this type (`box`), add all the units from these boxes to the total.
#       - Otherwise, load only as many boxes as the truck can hold, and then return the total number of units loaded.
# 4. **Return the Total Number of Units**:
#    - After processing all box types, return the total number of units loaded onto the truck.

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Step 1: Sort the box types based on the number of units per box in descending order
        boxTypes.sort(key=lambda x: -x[1])

        # Step 2: Initialize the total number of units to 0
        boxes = 0

        # Step 3: Traverse the sorted box types and load the truck greedily
        for box, unit in boxTypes:
            if truckSize > box:
                # Step 3.1: Load all the boxes of this type onto the truck
                boxes += box * unit
                truckSize -= box
            else:
                # Step 3.2: If the truck can't carry all the boxes, load as many as possible
                boxes += truckSize * unit
                return boxes

        # Step 4: Return the total number of units loaded
        return boxes
