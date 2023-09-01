"""

Purpose: Illustrate the built-in statistics of flowers in cucumbers.

VS Code Menu / View / Command Palette / Python Interpreter
Must be 3.10 or greater to get the correlation and linear regression.

Uses only Python Standard Library modules.

@ uses statistics module for descriptive stats
@ uses sys module for checking Python version

"""
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------


# Import from Python Standard Library

import statistics
import sys



# Datasets
femaleflowers = [1, 3, 3, 4, 5, 6, 7, 6, 9, 15, 11, 8]
totalflowers = [2, 6, 8, 20, 21, 23, 15, 27, 30, 31, 31, 22]

totalflowers_no = sum(totalflowers)
femaleflowers_no = sum(femaleflowers)

mean = statistics.mean(totalflowers)
median = statistics.median(totalflowers)
mode = statistics.mode(totalflowers)

var = statistics.variance(totalflowers)
stdev = statistics.stdev(totalflowers)
lowest = min(totalflowers)
highest = max(totalflowers)

# if the lists are not the same size,
# log an error and quit the program
if len(femaleflowers) != len(totalflowers):
    logger.error("ERROR: The related sets are not the same size.")
    logger.error(f" {len(femaleflowers)}!={len(totalflowers)}")
    quit()


logger.info("YAYY I DID MY TASK 5!!!")

logger.info(f"Total flowers numbers is {totalflowers_no}")
logger.info(f"Female flowers numbers is {femaleflowers_no}")

logger.info(f"mean = {mean:.1f}")
logger.info(f"median = {median:.1f}")
logger.info(f"mode = {mode:.1f}")
logger.info(f"var = {var:.2f}")
logger.info(f"stdev = {stdev:.2f}")
logger.info(f"lowest = {lowest:.0f}")
logger.info(f"highest = {highest:.0f}")