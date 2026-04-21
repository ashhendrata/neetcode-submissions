class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # index = number of times its been encountered
        counter = [set() for _ in range(len(nums) + 1)] 
        encountered = set() 
        for n in nums:
            if n not in encountered:
                counter[1].add(n)
            else:
                curr = 0
                for i, bucket in enumerate(counter):
                    if n in bucket:
                        bucket.discard(n)
                        curr = i
                        break
                counter[curr + 1].add(n)
            encountered.add(n)
        
        print(counter)
        
        num_values = 0
        res = []
        for i in range(len(nums), -1, -1):
            if num_values >= k:
                return res
            for num in counter[i]:
                res.append(num)
                num_values += 1
        return res
