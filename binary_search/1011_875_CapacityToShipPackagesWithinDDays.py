class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Solution lies between: max(weights) and sum(weights) so binary searching the range is good

        """
        min_capacity, max_capacity = max(weights), sum(weights)
        least_capacity = math.inf
        while min_capacity <= max_capacity:
            capacity = min_capacity + (max_capacity - min_capacity) // 2
            if self.is_possible_to_ship(weights, days, capacity):
                least_capacity = min(least_capacity, capacity)
                max_capacity = capacity - 1
            else:
                min_capacity = capacity + 1
        
        return least_capacity
    
    def is_possible_to_ship(self, weights, days, capacity): # 875
        total, days_count = 0, 1

        for weight in weights:
            total += weight
            if total > capacity: # very tricky
                days_count += 1
                total = weight
            
        return days_count <= days

