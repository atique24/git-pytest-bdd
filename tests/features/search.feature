Feature:Compare products
  As a consumer
  I can compare the products
  Before buying them


  Scenario Outline: Compare Mobile
    Given I am in the ecommerce website
    When I click on Mobile tab
    And I click on Add to Compare for <mobile1>
    And I click on Add to Compare for <mobile2>
    And I click compare button
    Then compare products page is displayed.
    Examples:
      | mobile1 | mobile2 |
      |SONY XPERIA| IPHONE|
