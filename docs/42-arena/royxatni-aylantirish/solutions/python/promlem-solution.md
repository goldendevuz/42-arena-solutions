# Promlem Solution

```python
def rotate(nums: list, k: int) -> list:
    for i in range(k):
        temp: int = nums[-1]
        for j in range(len(nums) - 1, -1, -1):
            nums[j] = nums[j - 1]
        nums[0] = temp
	  return nums
```

> **Time Complexity**: O(nk)
> 

> **Space Complexity**: O(1)
>