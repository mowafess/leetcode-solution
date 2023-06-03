class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        output = []
        
        while columnNumber:
            # need to subtract one from the column number 
            columnNumber, r = divmod(columnNumber - 1, 26)
            output.append(chr(65 + r))
            
        return "".join(output[::-1])