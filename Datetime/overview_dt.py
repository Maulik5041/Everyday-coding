"""Overview of the datetime module and different methods"""


from datetime import datetime
from datetime import date
from datetime import timedelta


# Understanding what it looks like
print(datetime.today())
# OUPUT: 2020-09-12 12:53:45.899493

print(date.today())
# OUTPUT: 2020-09-12

# Understanding the type of objects
today = datetime.today()
todaydate = date.today()

print(f'Type of today : {type(today)}\n\
Type of todaydate : {type(todaydate)}')
# OUTPUT: Type of today : <class 'datetime.datetime'>
#         Type of todaydate : <class 'datetime.date'>

# NOTE: Mixing these objects is not allowed

# Going deeper with the arguments
print(f'Month = {todaydate.month}\n\
Day = {todaydate.day}\n\
Year = {todaydate.year}')
# OUTPUT: Month = 9
#         Day = 12
#         Year = 2020

# Doing math with dates
# Assigining a date
christmas = date(2020, 12, 25)
print(f'Type of christmas object : {type(christmas)}\n\
Value of christmas : {christmas}')
# OUTPUT: Type of christmas object : <class 'datetime.date'>
#         Value of christmas : 2018-12-25

# A datetime object and date object cannot be used together in calculation
# print(f'Days remaining before christmas --> {christmas - today}')  # Fails
print(f'Days remaining before christmas --> {christmas - todaydate}')
# OUTPUT: Days remaining before christmas --> 104 days, 0:00:00

# This way of calculating a time difference has a specific name - timedelta
print(
    f'When calculating gap in days/time, we use {type(christmas - todaydate)}')
# OUTPUT: datetime.timedelta

# To get only a specific quantity from date method
print(f'Only {(christmas - todaydate).days} days to go for christmas')

# Understanding timedelta object
t = timedelta(days=4, hours=10)
print(f'Type of object --> {type(t)}')
print(f'Number of days = {t.days}')
# print(f'Number of hours = {t.hours}')  # Fails
# OUTPUT: Type of object --> <class 'datetime.timedelta'>
#         Number of days = 4
# AttributeError: 'datetime.timedelta' object has no attribute 'hours'

# NOTE: timedelta does not understand in hours. It understands only seconds.
#       It is basically a difference or gap between 2 given time stamps

print(f'Number of hours = {t.seconds/3600}')
# OUTPUT: Number of hours = 10.0

# A simple usecase of timedelta
eta = timedelta(hours=6)  # timedelta object
right_now = datetime.today()  # datetime object (NOT date object)

# Understand when to go out by adding these values
print(f'Go to the gym at {eta + right_now}')
# OUTPUT: Go to the gym at 2020-09-12 19:46:46.359487

# NOTE: Mixing timedelta object with datetime and date is allowed

print(
    f'My appointment for haircut is on {timedelta(days=3) + (date.today())}')
