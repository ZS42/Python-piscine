import time
from datetime import datetime

# Get the current time in seconds since January 1, 1970 from time library
#January 1, 1970 is also known as the Unix epoch but can name variable anything instaed of unix_epoch_time
unix_epoch_time = time.time()
print(f"Seconds since January 1, 1970: {unix_epoch_time:.4f} or {unix_epoch_time:2e}in scientific notation")
# Print the formatted date using strftime() using below format codes
# %b Month as locale’s abbreviated name.
# %d Day of the month as a zero-padded decimal number.
# %Y Year with century as a decimal number.
#for more format codes https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
#fromtimestamp() is a function. See after
formatted_date = datetime.fromtimestamp(unix_epoch_time).strftime("%b %d %Y")
print(formatted_date)

# The fromtimestamp() function is used to return the date corresponding to a specified timestamp.
# Note: Here the timestamp is ranging from the year 1970 to the year 2038, and this function does not consider leap seconds if any present in the timestamp. This function is a class method.
# Syntax: @classmethod fromtimestamp(timestamp)
# Parameters: This function accepts a parameter which is illustrated below:
# timestamp: This is the specified timestamp for which the date is going to be returned.
# Return values: This function returns the date corresponding to a specified timestamp.

