# @playpage
Feature: To test Play tab in Bookmyshow

  @tag3 @DateFilter
  Scenario Outline: User lands on Chennai Homepage and explores Play tab
    Given I hit Chennai URL and click on Play tab
    And I verify the play url
    When I click on Date option
    And I verify the "<Options>"
    Then I click on the Date Range
    And I click the right arrow till I reach "December 2025"
    Examples:
      | Options                                       |
      | Today & Tomorrow &  This Weekend & Date Range |
