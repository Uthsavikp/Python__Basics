'''
* @Author: Uthsavi KP
* @Date: 2020-12-30 22:21:02  
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-30 22:21:02
* @Title : To Get Day Of Week When Inputed Month,Day And Year
'''

def month_day_year(month,day,year,):
    new_year = int((year - (14 - month)) / 12)
    leap_year = int(new_year + (new_year/4) - (new_year/100) + (new_year/400)) 
    new_month = month + 12 * ((14 - month) / 12) - 2
    new_day = (day + leap_year + 31*(new_month) / 12) % 7   #Formula For Gregorian Calender
    day_of_week(new_day)
    return new_day
    
def day_of_week(new_day):
    switcher = {            # using dictionary to get the day
        0:'Sunday',
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday'
    }
    print(switcher.get(new_day, "Invalid day"))


if __name__ == "__main__":
    month = int(input("Enter Month: "))
    day =int(input("Enter Day: "))
    year =int(input("Enter Year: "))
    month_day_year(month,day,year)
