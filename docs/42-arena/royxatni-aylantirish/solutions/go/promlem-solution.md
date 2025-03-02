# Promlem Solution

```go
package main


func (_ Solution) MoveZeroes(nums []int) []int {
    var k = 0;
    for i := 0; i < len(nums); i++ {
        if nums[i] != 0 {
            nums[k], nums[i] = nums[i], nums[k]
            k++
        }
    }
    return nums;
}
```

> **Time Complexity**: O(nk)
> 

> **Space Complexity**: O(1)
>