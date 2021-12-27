class Solution:
    def compress(self, chars: List[str]) -> int:
        stack = []
        curr = ''
        count = 0
        output = []
        
        for ch in chars:
            if ch is curr:
                count += 1
                continue
            output += curr
            output += str(count) if count > 1 else ''
            curr = ch
            count = 1
            print(output)
       
        output += curr
        output += str(count) if count > 1 else ''
        
        for idx, ch in enumerate(output):
            chars[idx] = ch
            
        return len(output)