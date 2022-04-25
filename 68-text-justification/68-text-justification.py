class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        output = []
        line = []
        curr = 0
        
        def spaceOut(line, spaces, last=0):
            curr = 0
            limit = len(line)
            space = " "
            
            while spaces > 0:
                if curr == 0 or curr < limit - 1:
                    line[curr] += space
                    spaces -= 1
                curr += 1
                curr %= limit
            
            line.append(space * last)
            
            return "".join(line)
        
        
        for word in words:
            if curr + len(line) + len(word) > maxWidth:
                spaces = maxWidth - curr
                output.append(spaceOut(line, spaces))
                line = [word]
                curr = len(word)
            else:
                line.append(word)
                curr += len(word)
                
        if line:
            spaces = len(line) - 1
            left = maxWidth - curr - spaces
            output.append(spaceOut(line, spaces, left))
            
        return output
        
        
        # x = printLine(spaceOut(["This", "is", "an"], 8))
        # y = spaceOut([["example"], ["of"], ["text"]], 3)
        # z = spaceOut([["justification."]], 2)
        # print(*map(len, y))
        # print(*map(len, z))
        # print(x)
                
                
        