class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        lines = {}
        res = []
        
        for i, row in enumerate(rows):
            for ch in row:
                lines[ch] = i
        
        for word in words:
            _word = word.lower()
            first = lines[_word[0]]
            is_from_single_line = True
            
            for ch in _word:
                if lines[ch] != first:
                    is_from_single_line = False
                    break
                    
            if is_from_single_line:
                res.append(word)
                
        return res
        