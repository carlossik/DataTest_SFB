# Created by Carlos at 05/02/2019
Feature: Verifying Duplicate Values
  # Test for duplicate schools by Name, URN, and LAESTAB
  Scenario: Verify no duplicate school by Name
    Given I have the protocol list
    When I search for for shoools with Names
    Then there should be no duplicates loaded

     Scenario: Verify no duplicate school by URN
    Given I have the protocol list
    When I search for for shoools with URN
    Then there should be no duplicates loaded

   Scenario: Verify no duplicate school by LAESTAB
    Given I have the protocol list
    When I search for for shoools with LAESTAB
    Then there should be no duplicates loaded



















  Scenario:  Verifying Trust number match
  Given I have master sheet
  When I compare Value URN on master sheet to URN on dev
  Then There will be a match
    # Enter steps here

  Scenario: Verifying Trust Name match
    Given I have the master sheet
    When i compare Trust Name on File to trust name on dev
    Then There will be a match

    Scenario: Verifying All School Phases are represented correctly
      Given I have a master sheet
      When I compare school phase on file to phase on dev
      Then There will be a match

      Scenario: Verifying all school types are represented
        Given i have the master sheet
        When i compare school type on master sheet to dev
        Then There will be a match

        Scenario: Verifying LA count of schools
          Given i have the master sheet
          When i compare LA count  on master sheet to dev
          Then There will be a match

          Scenario: Verifying School Type


