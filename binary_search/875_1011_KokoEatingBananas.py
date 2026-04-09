from  math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        how many banans to eat per hour, SPEED: what's the minimum speed to finish all in h hours
        Note: 
        - once eating a pile in one hour, can't eat other piles in the extra leftover time
        - piles.length <= h so always we can finish it 

        solution lies between: 1 and max(piles) so let's binary search on this range

        """
        min_speed, max_speed = 1, max(piles)
        min_eating_speed = math.inf
        while min_speed <= max_speed:
            speed = min_speed + (max_speed - min_speed) // 2
            if self.possible_to_finish(piles, h, speed):
                min_eating_speed = min(min_eating_speed, speed)
                max_speed = speed - 1
            else:
                min_speed = speed + 1

        return min_eating_speed
    
    def possible_to_finish(self, piles, h, speed): # 1011
        count = 0
        # speed = distance / time, so time = distance / speed
        for pile in piles:
            count += math.ceil(pile / speed) # trick: very important
        return count <= h

            









