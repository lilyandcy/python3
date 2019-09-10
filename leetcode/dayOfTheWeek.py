class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        from datetime import datetime
        temp = ["Friday","Saturday","Sunday", "Monday", "Tuesday", "Wednesday","Thursday"]
        day1 = datetime.strptime('1971-01-01', '%Y-%m-%d')
        day2 = datetime.strptime(str(year) + '-' + str(month) + '-' + str(day), '%Y-%m-%d')
        return temp[(day2 - day1).days % 7]