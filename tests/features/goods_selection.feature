Feature: Test the goods selection functionality on amazon website

  @demo
  Scenario: Search for some goods and check if displayed in search result
    Given User is on the application home page
    When  User search for the product "LG 55 QNED 75 4K"
    Then  User should see the product in the list 'LG 55" QNED 75 4K QNED Smart TV (2023)'

  @demo
  Scenario: Select some goods and add to cart
    Given User is on the application home page
    When  User search for the product "LG 55 QNED 75 4K"
    Then  User should see the product in the list 'LG 55" QNED 75 4K QNED Smart TV (2023)'
    When  User adds the product 'LG 55" QNED 75 4K QNED Smart TV (2023)' into cart
    Then  User should see product 'LG 55" QNED 75 4K QNED Smart TV (2023)' in the shopping cart

