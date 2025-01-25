# Time Complexity: O(N log N), where N is number of stations
# Space Complexity: O(N) for heap and tracking

# INTUITION:
# Greedy approach to minimize refueling stops by:
# 1. Always moving as far as current fuel allows
# 2. Collecting station fuel capacities on the way
# 3. When stuck, use max collected fuel to extend range

# ALGO:
# 1. Start with initial fuel, track current position
# 2. While current fuel < target:
#    - Collect all reachable station fuel into max heap
#    - If no stations reachable and can't reach target: return -1
#    - Select max fuel station to refuel
#    - Increment refueling stops
# 3. Return total refueling stops needed

class Solution:
   def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
       # Immediate success if start fuel sufficient
       if startFuel >= target:
           return 0

       currentFuel = startFuel
       stationIndex = 0
       refuelingStops = 0
       maxFuelHeap = []

       while currentFuel < target:
           # Collect all reachable station fuels
           while stationIndex < len(stations) and stations[stationIndex][0] <= currentFuel:
               heapq.heappush(maxFuelHeap, -stations[stationIndex][1])
               stationIndex += 1

           # No way to proceed further
           if not maxFuelHeap:
               return -1

           # Refuel with max available fuel
           currentFuel += -heapq.heappop(maxFuelHeap)
           refuelingStops += 1

       return refuelingStops
