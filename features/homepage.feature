@homepage
Feature: Book My Show Home Page Verification

  @tag1
  Scenario: Launch Book my show
    Given I open the BookMyShow homepage

  @tag2
  Scenario Outline: User explores location options and selects Chennai
    Given I open the BookMyShow homepage
    Then I check if location box is open else open it
    And I enter "<locations>" in the search and assert the "<loc_suggestions>"
    Then I enter "Chenn" and I select Chennai from the dropdown
    And I land on Book my show chennai page
    Examples:
      | locations | loc_suggestions                          |
      | Chenn     | Chennai & Chennur                        |
    #  | pun       | Pune & Cherrapunji & Punalur & Punganur  |
    #  | Mumb      | Mumbai                                   |
    #  | Bengaluru | Bengaluru & Vijayapura (bengaluru Rural) |





