Feature: Amazon test
    Scenario: Add items to the cart
        Given I go to the amazon home page
        And I search for product "hats for men"
        When I add the first item to the cart with quantity "2"
#        And I open the cart
#        Then I verify that the total price and quantity are correct
#        And I reduce the quantity to "quantity"
#        Then I verify that the total price and quantity are correct