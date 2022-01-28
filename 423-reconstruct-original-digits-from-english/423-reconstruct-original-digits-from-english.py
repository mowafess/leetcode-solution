class Solution:
    def originalDigits(self, s: str) -> str:
        
        output = []
        freq_table = Counter(s)
        classifiers = [  ('z', '0', 'zero'), ('w', '2', 'two'), ('u', '4', 'four'), ('x', '6', 'six'),
                        ('g', '8', 'eight'), ('o', '1', 'one'), ('r', '3', 'three'), ('f', '5', 'five'),
                        ('v', '7', 'seven'), ('i', '9', 'nine')
                     ]
        
        for classifier, num, word in classifiers:
            if classifier in freq_table:
                freq = freq_table[classifier]
                for ch in word:
                    freq_table[ch] -= freq
                output.append(num * freq)
                
        return ''.join(sorted(output))
        