class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(word):
            arr = [*word]
            mid = len(word) // 2
            
            for i in range(mid):
                arr[i], arr[~i] = arr[~i], arr[i]
            
            return ''.join(arr)
        
        words = s.split()
        
        return ' '.join(map(reverse, words))
        