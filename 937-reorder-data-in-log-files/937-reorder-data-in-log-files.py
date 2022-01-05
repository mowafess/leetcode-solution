class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        digit_logs = []
        letter_logs = []
        
        for i, _log in enumerate(logs):
            log = _log.split(" ", maxsplit=1) 
            if log[1][0].isdigit():
                digit_logs.append(_log)
            else:
                idx = log[0]
                content = log[1]
                letter_logs.append((i, idx, content))
                
        letter_logs = [logs[log[0]] for log in sorted(letter_logs, key=lambda x: (x[2], x[1]))]
        
        return letter_logs + digit_logs
                
        
        