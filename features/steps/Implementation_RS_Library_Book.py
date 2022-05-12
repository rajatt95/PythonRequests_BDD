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

from Z_Utilities.Configurations import getConfig
from Z_Utilities.Resources import API_Resources


@given(u'the book details that needs to be added in the Library')
def step_impl(context):
    print("*************** the book details that needs to be added in the Library")
    print("****************** GIVEN")


@when(u'we execute the API - AddBook using POST HTTP method')
def step_impl(context):
    print("*************** we execute the API - AddBook using POST HTTP method")
    print("****************** WHEN")


@then(u'book is successfully added')
def step_impl(context):
    print("*************** book is successfully added")
    print("****************** THEN")
