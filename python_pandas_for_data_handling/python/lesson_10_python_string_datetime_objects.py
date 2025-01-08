# This is lesson 10 from Henrick Johansson's Master Pandas and Python for Data Handling

# Python Strings and Datetime Objects

# Python's datetime module is very useful for data handling purposes is mainly focused on output formatting and manipulation.
# DateTime calculations is a task with a high degree of complexity.

# Libraries - import the datetime madule as dt
import datetime as dt

# The Date Object
# Define date data either through a function or through data insertions (in this case integers can be created from string time
# data such as for example older standards such as 1988-11-24, or 24/11/1988, or 1988/24/11)
current_date = dt.date.today()
birth_date = dt.date(1988, 11, 24)

# Data Handling is often about unifying many such date and time standards into one standard for data analysis.
# Data files likely contain many different date standards, delivered as string or text data and the Data Handler will not only have to re-form these data
# files into a common form but also uinfy the different time and date standards into one standard for data analysis.
# The Datetime object is invaluable for these data handling operations.

# The datetime objects date attributes are accessible:
print(birth_date.month) # 11
print(birth_date.day) # 24
print(birth_date.year) # 1988
print(birth_date) # 1988-11-24
print(current_date) # 2024-12-24

# The time object is interesting when using time data or so-called event data. Remember: for data created before the datetime objects
# became common, time data and date data are often separate and exist in several columns, whereas modern datetime data often can be aggregated into
# a single column or entry per measurement or 'event'.  Administrative data is often centered on separate date and time data, and this is the main
# reason that date and time objects are used separately.
# Let's take a look at the time object...
obj_t = dt.time() # Instantiate a datetime time object at 00:00:00
print(obj_t) # Hours: minutes: seconds: milliseconds
print(dt.datetime.now()) # Date plus time, local time as default
# .now(tzinfor-Name) or we can make the datetime object aware using many different solutions, for example tzinfo-timezone or through other libraries.
# The Pandas Library has the most elegant solution in pd.Timestamp()

# Create a dat object with today's date (your local date, when you run this code)
local_today = dt.date.today()
print(local_today) # 2024-12-24

# Create a datetime object with today's date and zerotime
local_today = dt.datetime(local_today.year, local_today.month, local_today.day)
# Today's datetime date for year, month, and day.
print(local_today) # 2024-12-24 00:00:00

# The modern datetime object holds large amounts of useful data
current_datetime = dt.datetime.now()
print(current_datetime) # 2024-12-24 03:41:07.944256

# Use datetime to calculate the time today and now...
time_now = dt.datetime.now()
time_since_obt_t = time_now - local_today
print(time_since_obt_t) # 03:42:45.769167

# Remove the microseconds by zeroing them
time_since_obt_t -= dt.timedelta(microseconds = time_since_obt_t.microseconds)
print(time_since_obt_t) # 03:42:45

# jk: That is a pretty trippy syntax for timedelta.  The Python docs are the best explanation here: timedelta is a duration (interval I think in sql)
# jk: So that makes that make sense.  We get our full current local date time with zeroed time.  We then subtract now() - local_today, which now()
# jk: has the time component not zeroed, so the date drops and we get the time, but it has those pesky microseconds, so we use timedelta, specifying
# jk: the microseconds, then subtract from time with microseconds and Python does not display zeroed microseconds by default apparently.

# Calculate time differences using datetime objects
days_old = current_date - birth_date
days_old = days_old.days
print(days_old) # 13179

# Calculate time constructs such as years
years_old = days_old//365 # Note that days_old is a Python integer
print(years_old) # 36

# Real-world date, time, and datetime data...
# Real-world data may use other time formats than standard US/EU datetime and timezone data.   Data should either be converted to Datetime date
# or have relevant data extracted as strings and integer operations  to a suitable format for your particular purpose.
# Finding a good solution on how to handle time, old time standards is very important and is partly in the realm of subject matter expertise.

# Let's cut and paste some words from a coder experienced with datetimes

# Transparent timezone awareness always fail, unless you are 100% certain that a tzaware datetime object will remain unconverted 
# from the very top to the very bottom of the stack and all the way up again no matter who is reading and what they are doing.

# For longterm minimization of pain, bugs, and effort, you convert datetimes to UTC as early as possible and take them back to some 
# localized version as late as possible (in the frontend, for a webapp, so that the backend never needs to know there is 
# such a thing as timezones (except for separate validation and correction routines, since timezone definitions always end up being incorrect to 
# some degree when you use them at scale)).

# If the localization of the datetime is an essential aspect (such as the departure time of a ship leaving port), you store a UTC
# value together with a record of the location. Only at the latest possible moment of processing, should you do a lookup on the 
# location data to make a local time.

# Obviously, there will be exceptions to this rule. If you batch process billions of timestamps under a tight deadline and must do 
# calculations in local time, it might make sense to have the values persisted localized.

# Let's get back to Data Handling
# Data Handling together with the datetime module is so common that two special methods have been developed to handle DateTime objects input and output.
# If you are a great Data Handler, you likely don't need those methods but otherwise they may save you a lot of advanced code typing.

# Use the strftime method to edit output from Datetime objects which returns strings representing the datetime, controlled by an explicit
# format for the string.  In the manual, there is a large number of codes for different output and formatting.

# Reuse the time_now object with current date and time.
print(time_now)

# Date
ymd = time_now.strftime('%Y-%m-%d')
print('date:', ymd) # date: 2024-12-24

# Time
time = time_now.strftime('%H:%M:%S')
print('time:', time) # time: 04:24:56

# Datetime
datetime = time_now.strftime('%m/%d/%Y, %H:%M:%S')
print('datetime:', datetime) # datetime: 12/24/2024 04:25:38

# This is one way of many to format string output from the datetime object

# Let's look at the corresponding .strptime() method to format input to a datetime object from a string

# Create a string with an obscure date and time format
str_date_time = '06, June, 1999 12:45' # A string with date and time data.
# Print the String and its type
print('string', str_date_time) # string: '06, June, 1999 12:45'
print('type:', type(str_date_time)) # <class 'str'>

# Use .strptime() method to create a datetime object from the string. .strptime() needs an existing datetime object
dt_object = time_now.strptime(str_date_time, '%d, %B, %Y %H:%M')
print('datetime object:', dt_object) # datetime object: 1999-06-06 12:45:00
print('type:', type(dt_object)) # <class 'datetime.datetime'>

# In this video lecture you learned to create and use datetime objects, and you learned to calculate time durations using datetime objects.
# Time data in Data Handling is most of the time is either about defining the time of an event according to the time standard and use it with associated
# data values, or to use the calculated durations between two or more events, for example, the duration until the effect of a medical drug, or the total
# time of an experiment with event times within that time frame.
