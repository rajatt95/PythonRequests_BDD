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

# Created by rajatverma at 12/05/22
Feature: Execute the scenario with multiple data sets
  This feature is created to Execute the scenario with multiple data sets

  @Regression @BVT
  Scenario Outline: Login Scenario with multiple data sets
   # Given Do Sign in with "<email>" and "<password>"
     Given Do Sign in with <email> and <password>

      Examples:
        | email   | password   |
        | email_1 | password_1 |
        | email_2 | password_2 |
        | email_3 | password_3 |
        | email_4 | password_4 |
        | email_5 | password_5 |

  @Regression @Smoke @Sanity
  Scenario Outline: Login Scenario with multiple data sets
     Given Do Sign in with <email> and <password>

      Examples:
        | email   | password   |
        | email_6 | password_6 |
        | email_7 | password_7 |

  @Regression @Sanity
  Scenario Outline: Login Scenario with multiple data sets
     Given Do Sign in with <email> and <password>

      Examples:
        | email   | password   |
        | email_8 | password_8 |
        | email_8 | password_8 |









