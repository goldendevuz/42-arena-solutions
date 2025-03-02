# Promlem Solution

```js
function rotate(nums, k){
    for (let i = 0; i < k; i++) {
        const temp = nums[nums.length - 1]
        for (let j = nums.length - 1; j > 0; j--) {
            nums[j] = nums[j - 1]
        }
        nums[0] = temp
    }
    return nums
}

module.exports = {rotate}
```

> **Time Complexity**: O(n)
> 

> **Space Complexity**: O(1)
>