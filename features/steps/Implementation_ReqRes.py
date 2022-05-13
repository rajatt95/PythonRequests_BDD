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
import requests
from behave import *

from Z_Utilities.Resources import API_Resources
from Z_Utilities.CommonUtilties import getBaseURL_ReqRes


@given('Execute the API - List Users using GET HTTP method')
def step_impl(context):
    # GET request
    context.response = requests.get('https://reqres.in/api/users?page=2')
    print('https://reqres.in/api/users?page=2')
    print("")
    # context.response = requests.get(getBaseURL_ReqRes() + API_Resources.GET_LIST_ALL_USERS)
    # print(getBaseURL_ReqRes() + API_Resources.GET_LIST_ALL_USERS)

@given('Execute the API - Single User using GET HTTP method')
def step_impl(context):
    # GET request
    context.response = requests.get('https://reqres.in/api/users/2')
    print('https://reqres.in/api/api/users/2')
    print("")
    # context.response = requests.get(getBaseURL_ReqRes() + API_Resources.GET_LIST_SINGLE_USER)
    # print(getBaseURL_ReqRes() + API_Resources.GET_LIST_SINGLE_USER)


################################################

# Common Step Definitions

# age:d -> This will be treated as integer
# @given('Do Sign in with {age:d}')
@then('Response Status Code should be {expectedStatusCode:d}')
def step_impl(context, expectedStatusCode):

    # Expected
    print("{} {}".format("Expected Response Status code ->", expectedStatusCode))
    # Actual
    print("{} {}".format("Actual Response Status code ->", context.response.status_code))
    print("")
    assert context.response.status_code == expectedStatusCode


@then(u'Response Headers should have key {expectedHeaderKey} and value {expectedHeaderValue}')
def step_impl(context, expectedHeaderKey, expectedHeaderValue):

    # Remove '' from headerKey and headerValue
    expectedHeaderKey = expectedHeaderKey.replace("'", "")
    expectedHeaderValue = expectedHeaderValue.replace("'", "")

    # Expected
    print("Expected Response Header -> Key: "+expectedHeaderKey+", Value:"+expectedHeaderValue)
    # Actual
    print("Actual Response Header -> , Key: "+expectedHeaderKey+", Value:" + context.response.headers[expectedHeaderKey])
    assert context.response.headers[expectedHeaderKey] == expectedHeaderValue
    print("")

# @then('Response Headers should have key {headerKey} and value {headerValue}')
# def step_impl(context, headerKey, headerValue):
#     # print("context.response['headerKey']: "+context.response['headerKey'])  #
#     print(headerKey)
#     print(headerValue)
#     print("")
