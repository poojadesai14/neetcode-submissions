class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        minheap = []

        for num, count in freq.items():
            heapq.heappush(minheap,(count,num))

            if len(minheap)>k:
                heapq.heappop(minheap)

        result = []

        while minheap:
            count, num = heapq.heappop(minheap)
            result.append(num)

        return result    

        