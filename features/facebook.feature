Feature: Facebook sign up tests

    Scenario: Sign up successfully as male
        Given I go to the Facebook home page
        And I click on sign up
        When I complete the sign up form with valid name, last name, email, password and birth date
        And I select Male as gender
        And I click on Register
        Then I am able to create an account

    Scenario: Sign up successfully as female
        Given I go to the Facebook home page
        And I click on sign up
        When I complete the sign up form with valid name, last name, email, password and birth date
        And I select Female as gender
        And I click on Register
        Then I am able to create an account

    Scenario: Sign up successfully as personalized
        Given I go to the Facebook home page
        And I click on sign up
        When I complete the sign up form with valid name, last name, email, password and birth date
        And I select Personalized as gender
        And I select a pronoun
        And I click on Register
        Then I am able to create an account

    Scenario: Sign up using the current date as birth date
        Given I go to the Facebook home page
        And I click on sign up
        When I complete the sign up form using the current date as birth date
        And I click on Register
        Then I get an error indicating that the birth date is not correct

    Scenario: Sign up using an invalid email
        Given I go to the Facebook home page
        And I click on sign up
        When I complete the sign up form using an email address without @
        And I click on Register
        Then I get an error indicating that the email is not correct

    Scenario: Sign up using an invalid phone
        Given I go to the Facebook home page
        And I click on sign up
        When I complete the sign up form using an invalid phone number
        And I click on Register
        Then I get an error indicating that the phone number is not correct

    Scenario: Sign up using an chinese chars
        Given I go to the Facebook home page
        And I click on sign up
        When I complete the sign up form with valid name, last name using chinese characters
        And I click on Register
        Then I am able to create an account

    Scenario: Validate mandatory fields
        Given I go to the Facebook home page
        And I click on sign up
        When I click on Register
        Then I get messages indicating all mandatory fields