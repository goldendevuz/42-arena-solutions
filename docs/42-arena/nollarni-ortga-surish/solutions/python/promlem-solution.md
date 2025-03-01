# Promlem Solution

```python
def moveZeroes(nums: list) -> list:
  k: int = 0
  for i in range(len(nums)):
    if nums[i]:
      nums[k], nums[i] = nums[i], nums[k]
      k += 1
  return nums
```

> **Time Complexity**: O(n)
> 

> **Space Complexity**: O(1)
>