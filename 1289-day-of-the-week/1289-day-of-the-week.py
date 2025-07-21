class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # 1971.01.01 ==> Friday
        days = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]

        leaps = set(yr for yr in range(1968, 2100, 4))
        month_days = [0, 31, 29 if year in leaps else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        days_later = 0

        for y in range(1971, year):
            days_later += (366 if y in leaps else 365)
        
        for m in range(1, month):
            days_later += month_days[m]

        return days[(day + days_later) % 7]
        
        