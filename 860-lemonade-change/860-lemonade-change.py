class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        freq = Counter()
        
        def isThereChange(table, amount):
            output = [False, {}]
            
            if amount == 5:
                output[0] = True
            
            if amount == 10 and table[5]:
                output[0] = True
                output[1][5] = 1
            
            if amount == 20 and freq[5] and freq[10]:
                output[0] = True
                output[1][5] = 1
                output[1][10] = 1
            elif amount == 20 and freq[5] > 2:
                output[0] = True
                output[1][5] = 3
                
            return output
          
        
        for bill in bills:
            flag, change = isThereChange(freq, bill)
            if not flag:
                return False
            # print(change)
            for change_bill, times in change.items():
                freq[change_bill] -= times
            
            freq[bill] += 1

        return True
        