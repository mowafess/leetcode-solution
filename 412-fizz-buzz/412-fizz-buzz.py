class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        output = []
        
        for i in range(1, n + 1):
            curr = str(i)
            
            if not i % 15:
                curr = "FizzBuzz"
            elif not i % 5:
                curr = "Buzz"
            elif not i % 3:
                curr = "Fizz"
                
            output.append(curr)
            
        return output
            