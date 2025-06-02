@eventpg
Feature: To test Events Page in Bookmyshow
  # Enter feature description here
  @tag4
  Scenario Outline: To verify the Price tab with price range 0 - 500 and check for count of no: championships, competitions and show
    Given I am in Price tab page
    When I select Price filter
    And I verify the range values "<options>"
    Then I click on "0 - 500"
    When I click on the 3rd card
    And I book it
    Then I click on the 2nd date
    And I click on the 1st time slot
    And I click on proceed button
    When I click on add tickets
    Then I add 2 tickets
    And I click on proceed button
    Then I click on "<seats>"
    Examples:
      | options                                  | seats |
      | Free & 0 - 500 & 501 - 2000 & Above 2000 | 3     |

  @tag5
  Scenario Outline: To verify the Price tab with price range 0 - 500 and check for count of no: championships, competitions and show
    Given I am in Price tab page
    When I select Price filter
    And I verify the range values "<options>"
    Then I click on "0 - 500"
    When I click on the card "Rambo Circus"
    And I book it
    Then I click on the 2nd date
    And I click on the 1st time slot
    And I click on proceed button
    Then I click on "<seats>"
    Examples:
      | options                                  | seats |
      | Free & 0 - 500 & 501 - 2000 & Above 2000 | 3     |