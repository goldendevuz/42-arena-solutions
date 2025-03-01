# Promlem Solution

```java
package solution;

import java.util.*;

class Solution {
    public int[] moveZeroes(int[] nums) {
        int k = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                int temp = nums[k];
                nums[k] = nums[i];
                nums[i] = temp;
                k ++;
            }
        }
        return nums;
    }
}
```

> **Time Complexity**: O(n)
> 

> **Space Complexity**: O(1)
>