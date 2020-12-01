
@registration
Feature: ecommerce website
  As a buyer,
  I want to search mobile/TV online
  So I can buy mobile or TV


  Scenario Outline: Registration
    Given I am in the ecommerce website
    When I click on Account
    And I select Register option from dropdown menu
    And I enter "<firstname>" "<lastname>" "<email>" "<password>" "<confirm>"
    And I select the checkbox
    And I click the Register button
    Then I see the "<success>" message

    Examples: Registration
      | firstname | lastname | email             | password| confirm | success                                           |
      | Test      | twentyfive |test@twentyfive.com|test12345|test12345| Thank you for registering with Main Website Store.|