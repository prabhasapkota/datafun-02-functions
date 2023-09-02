"""
Author = Prabha Sapkota    
Date = 08-31-2023
Purpose: Attempting Task 4 to write defensive functions by using math module, 
and if things don't work provide a custom message.

"""

import math

from util_logger import setup_logger
logger, logname = setup_logger(__file__)


def get_field_area(height, width):
    """
    Return area of a rectangular experimental field where biological experiment is designed given the height and width.
    Args:
    @param height: the height of the field, width: the width of field
    @return: the area of the field
    @raise Exception: if height, width is not a number

    """

    
    logger.info(f"CALLING get_field_area({height, width})")

    try: 
        area = height * width 
        logger.info(f"The field area is {area}sq.m")
        return area
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    
def get_field_areas_given_dimensions(height, width):
    """
    This function should return the area of a rectangle experimental field given its height and width.

    Keyword arguments:
    width -- the width of the field
    height -- the height of the field
    """
    # Implement the calculation logic here
    return width * height


def get_field_areas_given_list(height_list, width_list):
    """
    This function should return a list with the area of each experimental rectangular field.
    """

    logger.info(f"CALLING get_field_areas_given_lists({height_list, width_list})")

    if not height_list or not width_list:
        logger.error("Please add some items to the lists. Nothing to do.")
        quit()  # Quit the program

    if len(height_list) != len(width_list):
        logger.error("The number of height values must match the number of width values.")
        quit()  # Quit the program

    
    area_list = [] # empty list to hold the areas

    # for every pair of height and width values in the lists 
    for height, width in zip(height_list, width_list): 
        try:
            area = get_field_areas_given_dimensions(height, width)
            logger.info(f"height = {height}, width = {width}, area={area}")
            area_list.append(area)

        except Exception as ex:
            logger.error(f"height = {height}, width = {width}, Error: {ex}")



def get_total_plantsnumbers(plantnumbers_list):
    """
    This function should return a total plantnumbers in a field.
    
    """
    logger.info(f"CALLING get_total_plantnumbers({plantnumbers_list})") 

    try:
         total = math.fsum(plantnumbers_list)
         logger.info(f"Total plantnumbers is {total}")
         return total
    except Exception as ex:
         logger.error(f"Error: {ex}")
         return None

   


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# Literally: "if this module name == the name of the main running module"
# (as opposed to being imported by another module like we do the logger),
# then, follow these instructions.
if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(6,2) = {math.comb(6,2)}")
    logger.info(f"math.perm(6,2) = {math.perm(6,2)}")

    logger.info("")

    logger.info("TRY: Call get_leaf_area_given_height()_and_width() function with a different values.")
    get_field_area(50,20)
    get_field_area(64,51)
    get_field_area(33, 21)
    logger.info("")

    logger.info("TRY: Call get_leaf_area_list() function with a list of values")
    height_list = [39, 38, 60, 80, 45, 58]
    width_list = [23, 19, 38, 22, 44, 35]
    get_field_areas_given_list(height_list, width_list)
    logger.info("")
    
    logger.info("TRY: Call get_total_leafnumbers() function with a different values")
    total_plantnumbers_list = [31, 87, 220, 102, 58]
    get_total_plantsnumbers(total_plantnumbers_list)
    logger.info("")
    
    print("Done. Please check the log file for more details.")


