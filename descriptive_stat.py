""
#Purpose : "To calculate and compare the measures of central tendency for two datasets."
""

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)
# Import from Python Standard Library

import statistics


data_s1 = [10, 11, 14, 20, 20, 20, 22, 24, 28, 31]

mean_s1= statistics.mean(data_s1)
median_s1 = statistics.median(data_s1)
mode_s1 = statistics.mode(data_s1)
variance_s1= statistics.pvariance(data_s1)

data_s2 = [2, 9, 13, 14, 20, 20, 24, 26, 32, 40]
mean_s2 = statistics.mean(data_s2)
median_s2 = statistics.median(data_s2)
mode_s2 = statistics.mode(data_s2)

print ("Mean of data s1 = ", mean_s1)
print ("Median of data s1 =  ", median_s1)
print ("Mode of data s1 = ", mode_s1)

print ("Mean of data s2 = ", mean_s2)
print ("Median of data s2 =  ", median_s2)
print ("Mode of data s2 = ", mode_s2)

