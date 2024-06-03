# Promlem Solution

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [
            "FizzBuzz" if number % 15 == 0
            else "Fizz" if number % 3 == 0
            else "Buzz" if number % 5 == 0
            else str(number)
            for number in range(1, n+1)
        ]
```