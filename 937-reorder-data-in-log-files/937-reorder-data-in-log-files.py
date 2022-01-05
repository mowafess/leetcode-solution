class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        digit_logs = []
        letter_logs = []
        
        for i, log in enumerate(logs):
            idx, content = log.split(" ", maxsplit=1) 
            if content[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((i, idx, content))
                
        letter_logs = [logs[log[0]] for log in sorted(letter_logs, key=lambda x: (x[2], x[1]))]
        
        return letter_logs + digit_logs
    
    
# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         def get_key(log):
#             _id, rest = log.split(" ", maxsplit=1)
#             return (0, rest, _id) if rest[0].isalpha() else (1, None, None )
#         result = sorted(logs, key=get_key)
#         return result

                
        
        