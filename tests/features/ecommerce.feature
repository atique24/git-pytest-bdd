
@mobile               #feature level tag
Feature: ecommerce website
  As a buyer,
  I want to search mobile/TV online
  So I can buy mobile or TV

  @sortBy              #scenario level tag
  Scenario Outline: Check Sort By functionality
    Given I am in the ecommerce website
    When I click on Mobile Tab
    And I select Sort By "<Name>"
    Then all the available mobiles are sorted by "<result>"
    Examples:
      | Name     | result                                 |
      | Name     | [IPHONE, SAMSUNG GALAXY1, SONY XPERIA]  |
      | Price    | [SONY XPERIA, SAMSUNG GALAXY2, IPHONE]  |
      | Position | [SONY XPERIA, IPHONE, SAMSUNG GALAXY3]  |


  Scenario: Check Mobile Phone
    Given I am in the ecommerce website
    When I click on Mobile Tab
    Then all available mobiles are displayed











