# Promlem Solution

```java
package main


func (_ Solution) Rotate(nums []int, k int) []int {
    for i := 0; i < k; i++ {
        var temp int = nums[len(nums) - 1]
        for j := len(nums) - 1; j > 0; j-- {
            nums[j] = nums[j - 1]
        }
        nums[0] = temp
    }
    return nums
}
```

> **Time Complexity**: O(nk)
> 

> **Space Complexity**: O(1)
>