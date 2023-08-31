"""
Author = Prabha Sapkota    
Date = 08-31-2023
Purpose: Illustrate the math module and how to write
defensive functions by trying them, 
and if things don't work provide a custom message.

Use try / except / finally whenever a valid function could cause an error
e.g.,
- a number is not valid such as a negative radius or age
- a string is empty or missing
- the requested resource could not be found

@ uses math module - for some advanced math

"""

import math

from util_logger import setup_logger
logger, logname = setup_logger(__file__)


def get_leaf_area(height, width):
    """
    Return area of a leaf given the height and width.

    @param height: the height of the leaf, width: the width of leaf
    @return: the area of the leaf
    @raise Exception: if height, widhth is not a number

    """

    
    logger.info(f"CALLING get_leaf_area({height, width})")

    try: 
        area = height * width 
        logger.info(f"The leaf area is {area}cm*cm")
        return area
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    
def get_leaf_areas_given_dimensions(height, width):
    """
    This function should return the area of a rectangle given its width and height

    Keyword arguments:
    width -- the width of the leaf
    height -- the height of the leaf
    """
    # Implement the calculation logic here
    return width * height


def get_leaf_areas_given_list(height_list, width_list):
    """
    This function should return a list with the area of each leaf.
    """

    logger.info(f"CALLING get_leaf_areas_given_lists({height_list, width_list})")

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
            area = get_leaf_areas_given_dimensions(height, width)
            logger.info(f"height = {height}, width = {width}, area={area}")
            area_list.append(area)

        except Exception as ex:
            logger.error(f"height = {height}, width = {width}, Error: {ex}")



def get_total_leafnumbers(leafnumbers_list):
    """
    This function should return a list with leafnumbers in a plant.
    
    """
    logger.info(f"CALLING get_total_leafnumbers({leafnumbers_list})") 

    try:
         total = sum(leafnumbers_list)
         logger.info(f"Total leafnumbers is {total}")
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
    get_leaf_area(4,2)
    get_leaf_area(6,5)
    get_leaf_area(3, 2)
    logger.info("")

    logger.info("TRY: Call get_leaf_area_list() function with a list of values")
    height_list = [9, 3, 6, 8, 4, 5]
    width_list = [2, 1, 3, 2, 4, 3]
    get_leaf_areas_given_list(height_list, width_list)
    logger.info("")
    
    logger.info("TRY: Call get_total_leafnumbers() function with a different values")
    total_leafnumbers_list = [3, 4, 2, 10, 5]
    get_total_leafnumbers(total_leafnumbers_list)
    
    print("Done. Please check the log file for more details.")


