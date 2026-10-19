# Travel Fare Calculator

## Description
This program calculates the total travel fare based on the passenger name, travel distance in kilometers, and the number of passengers at a fixed fare rate.

## Version 1 - Original code without input validation
- Input : Accepts passenger name, distance (km), and the number of passengers[cite: 5].
- Process : Multiplies the distance by the fare rate (PHP 14) and the number of passengers to compute the total fare[cite: 5].
- Output : Displays the passenger name and the rounded total fare in PHP[cite: 5].
- Note : Does not include input validation.

## Version 2 - Updated code with input validation
- Input : Accepts passenger name, distance, and number of passengers with strict validation checks:
  - Passenger Name : Validates that the input is not empty[cite: 5].
  - Distance : Validates that the input is a valid number greater than 0[cite: 5].
  - Number of Passengers : Validates that the input is a positive whole number[cite: 5].
- Process : Loops until valid inputs are provided, prevents program crashes from incorrect data types, and computes the total fare.
- Output : Displays error messages for invalid entries and successfully shows the passenger name and calculated total fare upon valid entry.
