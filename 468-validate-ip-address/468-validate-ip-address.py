class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        v6_chars = "abcdefABCDEF"
        
        def isValidv4(s):
            if not s or len(s) > 3 or (s[0] == "0" and len(s) > 1):
                return False
            
            if not all(ch.isdigit() for ch in s):
                return False

            return 0 <= int(s) < 256
        
        def isValidv6(s):
            print(s)
            if 0 < len(s) < 5:
                return all(ch.isdigit() or ch in v6_chars for ch in s)
            return False

        
        if queryIP.count('.') == 3:
            ip = queryIP.split('.')
            if all(isValidv4(part) for part in ip):
                return 'IPv4'
        
        if queryIP.count(':') == 7:
            ip = queryIP.split(':')
            print(ip)
            if all(isValidv6(part) for part in ip):
                return "IPv6"
        
        return "Neither"
            
        