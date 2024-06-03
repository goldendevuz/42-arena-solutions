# Promlem Solution

```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:index + 1]) for index, num in enumerate(nums)]
```

> **Time Complexity**: O(n^2)
> 

> **Space Complexity**: O(n)
>