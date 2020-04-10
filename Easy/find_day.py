"""
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"

Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"

Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"

 

Constraints:

    The given dates are valid dates between the years 1971 and 2100.
"""

# 01-01-1971 is a Friday

class Solution:
    def dayOfTheWeek(self, day, month, year):
    	day_of_week = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']
        # new_dotw  = day_of_week[1:] + day_of_week[0]
    	days_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    	day_count = 0
    	for i in range(1971, year):
    		if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
    			day_count += 366
    		else:
    			day_count += 365

    	if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    		days_of_month[2] += 1

    	return day_of_week[(day_count + sum(days_of_month[:month]) + day) % 7]


s = Solution()

print(s.dayOfTheWeek(28, 3, 1999))
    	
