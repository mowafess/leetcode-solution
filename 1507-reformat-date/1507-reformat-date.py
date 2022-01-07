class Solution:
    def reformatDate(self, date: str) -> str:
        
        MONTH = { "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05",
                  "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10",
                  "Nov": "11", "Dec": "12" }
        
        dd, mm, yyyy = date.split()
        
        return '-'.join((yyyy, MONTH.get(mm), dd.zfill(4)[:-2]))