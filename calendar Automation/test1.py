# import re

# # open a text file
# f = open("evnt.txt", 'r')

# # extract the file's content
# content = f.read()
# print(content)
# # a regular expression pattern to match dates
# pattern = "\d{2}[/.-]\d{2}[/.-]\d{4}"


# # find all the strings that match the pattern
# dates = re.findall(pattern, content)

# for date in dates:
#     print(date)

# f.close()
# from datetime import datetime, timedelta
from datetime import datetime
msg = "/inp DP Practice, 30-7-23,9am-12pm,Discord"
arr = msg[4:].split(",")


# date_time_obj = datetime.strftime(arr[1], '%dd-%m-%yy')

st_date = arr[1].replace("-","/")

datetime_str = '09/19/22 13:55:26'

datetime_object = datetime.strptime("7/28/14", '%m/%d/%y')

print(type(datetime_object))
print(datetime_object)  # printed in default format