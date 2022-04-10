
### DOCUMENTATION ###
# https://docs.python.org/3/library/datetime.html

# Understand the difference between:
# Naives datetime are the easiest

import datetime

#datetime.date -> years, months, days
d = datetime.date(2016, 7, 29) # no zeros -> SinxtaxError 
print(d) # 2016-07-29

tday = datetime.date.today()
print(tday)

# Get the day of the week (2 options):
# 1. weekday: Monday 0 and Sunday 6
# 2. isoweekday: Monday 1 and Sunday 7
print(tday.weekday())
print(tday.isowwekday())

# Time deltas: difference between dates
tdelta = datetime.timedelta(days=7)

print(tday + tdelta) #will ad 7 days to today datetime

#i.e: one week ago
print(tday - tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2
bday = datetime.date(2016, 9, 24)

till_bday = bday - today
print(till_bday.days)

#print the n of microseconds
print(till_bday.todal_seconds())

# Datetime.date: working with year, month, day

#datetime.time -> hours, minutes, seconds and microseconds
t = datetime.time(9, 30, 45, 10000) #hours, minutes, seconds and microseconds

#Datetime.datetime: access to verything:
#years, month, days, hours, minutes, seconds and microseconds
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt.time())

tdelta = datetime.timedelta(days=7)
print(dt + tdelta) #will add 7 days to dt

tdelta = datetime.timedelta(hours=12)
print(dt + tdelta) #will add 12 hours to dt

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today) #current local datetime without a timezone
print(dt_now) #current local datetime without a timezone
print(dt_utcnow)

## pytz library

dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)
# 2016-07-12 12:30:45+00:00 

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

#Convert a datetime to a specific datetime (i.e:Denver)
dt_mtn = dt_now.astimezone(pytz.timezone('US/Mountain'))
print(dt)
print(dt_mtn)
# 2016-07-12 12:30:45+00:00 #UTC time
# 2016-07-12 06:30:45-06:00 #timezone

# Convert my naive datetime to another
dt_mtn = datetime.datetime.now()

mtn_tz = pytz.timezone('US/Mountain')  
dt_mtn = mtn_tz.localize(dt_mtn)

#pytz all timezones:

for tz in pytz.all_timezones:
	print(tz)


