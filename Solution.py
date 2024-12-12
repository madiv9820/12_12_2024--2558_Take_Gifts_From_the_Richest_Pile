from typing import List
import heapq, math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Convert all gift values to negative for max-heap behavior using min-heap
        gifts = [-x for x in gifts]
        # Heapify the list to organize it as a heap
        heapq.heapify(gifts)

        # Perform the gift operation k times
        for _ in range(k):
            # Pop the maximum gift value (which is the smallest in the negative list)
            x = heapq.heappop(gifts)
            # Take the square root of the gift value (after converting it back to positive)
            x = int(math.sqrt(-x))
            # Push the transformed gift value back to the heap (make it negative again)
            heapq.heappush(gifts, -x)

        # Initialize variable to accumulate the remaining gift values
        gifts_Left = 0

        # Sum all the remaining gift values after k operations
        while len(gifts) > 0:  gifts_Left += -heapq.heappop(gifts)  # Convert back to positive while summing

        # Return the total value of remaining gifts
        return gifts_Left