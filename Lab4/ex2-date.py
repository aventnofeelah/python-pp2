import datetime

#1
curr_date = datetime.datetime.now()
new_date = curr_date - datetime.timedelta(days=5)
print(new_date)

#2
curr_date = datetime.datetime.now()
tmrw_date = curr_date + datetime.timedelta(days=1)
ystr_date = curr_date - datetime.timedelta(days=1)
print(tmrw_date)
print(ystr_date)

#3
curr_date = datetime.datetime.now()
print(curr_date.year, "-", curr_date.month, "-", curr_date.day, sep="")
print(curr_date.strftime("%x"))

#4
date1_y = int(input("Enter first date year: "))
date1_m = int(input("Enter first date month: "))
date1_d = int(input("Enter first date day: "))
date2_y = int(input("Enter second date year: "))
date2_m = int(input("Enter second date month: "))
date2_d = int(input("Enter second date day: "))
y_diff = abs(date1_y - date2_y)
m_diff = abs(date1_m - date2_m)
d_diff = abs(date1_d - date2_d)
print(y_diff * 365 * 24 * 60 * 60 + m_diff * 30 * 24 * 60 * 60 + d_diff * 24 * 60 * 60)