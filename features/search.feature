Feature:Search Functionality

  @search
  Scenario: Search for a valid product
    Given I got navigated to Home Page
    When I enter valid product say "HP" into the search box field
    And I click on Search button
    Then Valid product should get displayed in Search results

  @search
  Scenario: Search for an invalid product
    Given I got navigated to Home Page
    When I enter invalid product say "Honda" into the search box field
    And I click on Search button
    Then proper message should be displayed in search results

  @search
  Scenario: Search without entering any product
    Given I got navigated to Home Page
    When I dont enter anything into search box field
    And I click on Search button
    Then proper message should be displayed in search results