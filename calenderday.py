from art import tprint
import calendar
tprint("ITS A DAY TELLING PROGRAM")

year = int(input("YEAR: "))
month = int(input("MONTH: "))
date = int(input("DATE: "))

output = calendar.weekday(year, month, date)

def calculation():
    if output == 1:
        tprint("DAY IS MONDAY", font="bulbhead")
    elif output == 2:
        tprint("DAY IS TUESDAY", font="bulbhead")
    elif output == 3:
        tprint("DAY IS WEDNESDAY", font="bulbhead")
    elif output == 4:
        tprint("DAY IS THURSDAY", font="bulbhead")
    elif output == 5:
        tprint("DAY IS FRIDAY", font="bulbhead")
    elif output == 6:
        tprint("DAY IS SATURDAY", font="bulbhead")
    elif output == 7:
        tprint("DAY IS SUNDAY", font="bulbhead")
  