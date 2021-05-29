Feature: Amazon test
    @AUTOMATED
    Scenario: Add items to the cart
        Given I go to the amazon home page
        And I search for product "hats for men"
        When I add the first item to the cart with quantity "2"
        And I open the cart
        Then I verify that the total price and quantity are correct
        And I select "1" as quantity
        Then I verify that the total price and quantity are correct