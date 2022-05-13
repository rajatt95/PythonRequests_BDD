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

from behave import *


# age:d -> This will be treated as integer
# @given('Do Sign in with {age:d}')

@given('Do Sign in with {email} and {password}')
def step_impl(context, email, password):
    print("var_email: " + email)
    print("var_password: " + password)
    print("")
