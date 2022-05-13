## /**
## * @author Rajat Verma
## * https://www.linkedin.com/in/rajat-v-3b0685128/
## * https://github.com/rajatt95
## * https://rajatt95.github.io/
## *
## * Course: Learn API Automation Testing with Python & BDD Framework (https://www.udemy.com/course/python-sdet-rest-api-automation/)
## * Tutor: Rahul Shetty (https://www.udemy.com/user/rahul445/)
## */
##
## /***************************************************/
#
# Created by rajatverma at 13/05/22
# https://reqres.in/
Feature: Verify the ReqRes API
  This feature is created to validate the functionality of ReqRes APIs

  Scenario: Verify functionality of API - List Users
    Given Execute the API - List Users using GET HTTP method
    # Common methods
    Then Response Status Code should be 200
    And Response Headers should have key 'Content-Type' and value 'application/json; charset=utf-8'
    And Response Headers should have key 'X-Powered-By' and value 'Express'

Scenario: Verify functionality of API - Single User
    Given Execute the API - Single User using GET HTTP method
    # Common methods
    Then Response Status Code should be 200
    And Response Headers should have key 'Content-Type' and value 'application/json; charset=utf-8'


