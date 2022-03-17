class Element(str):
    def __lt__(self, other):
        return int(self) < int(other)
    
    def __gt__(self, other):
        return int(self) > int(other)

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        # map numbers
        # extract first k elements
        # heapify
        
        nums = [*map(lambda num: Element(num), nums)]
        heap = nums[:k] 
        
        # return heapq.nlargest(k, nums)[-1]
        
        heapq.heapify(heap)
        
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heapq.heappop(heap)
        