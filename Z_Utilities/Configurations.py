# /**
# * @author Rajat Verma
# * https://www.linkedin.com/in/rajat-v-3b0685128/
# * https://github.com/rajatt95
# * https://rajatt95.github.io/
# *
# * Course: Learn API Automation Testing with Python & BDD Framework (https://www.udemy.com/course/python-sdet-rest-api-automation/)
# * Tutor: Rahul Shetty (https://www.udemy.com/user/rahul445/)
# */
#
# /***************************************************/

import configparser


def getConfig():
    config = configparser.ConfigParser()
    # read() -> Method to read the data from .ini file
    # As an argument -> We have to give the path of the file
    config.read('../Z_Utilities/properties.ini')
    return config











