class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        license = s.replace("-", "").upper()
        output = []
        
        for i in range(len(license), 0, -k):
            output.append(license[max(0, i-k):i])
            
        return "-".join(output[::-1])
            
        