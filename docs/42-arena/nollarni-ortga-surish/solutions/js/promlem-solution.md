# Promlem Solution

```js
function moveZeroes(nums){
    let k = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) {
      [nums[k], nums[i]] = [nums[i], nums[k]];
      k ++;
    }
  }
  return nums;
}

module.exports = {moveZeroes}
```

> **Time Complexity**: O(n)
> 

> **Space Complexity**: O(1)
>