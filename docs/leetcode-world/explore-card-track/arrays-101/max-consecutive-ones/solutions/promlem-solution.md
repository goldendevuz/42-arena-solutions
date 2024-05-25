# Promlem Solution

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count: int = 0
        max_count: int = 0
        for num in nums:
            if num:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        max_count = max(max_count, count)
        return max_count
```