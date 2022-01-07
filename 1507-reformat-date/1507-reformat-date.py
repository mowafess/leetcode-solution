class Solution:
    def reformatDate(self, date: str) -> str:
        
        MONTH = [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ]
        
        dd, mm, yyyy = date.split()
        
        return '-'.join((yyyy, str(MONTH.index(mm) + 1).zfill(2), dd.zfill(4)[:-2]))