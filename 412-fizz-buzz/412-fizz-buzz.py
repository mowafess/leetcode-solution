class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        i = 1
        output = []
        while i <= n:
            output.append("FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i))
            i += 1
            
        return output
            