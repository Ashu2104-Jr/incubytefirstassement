Incubyte String Calculator Kata Assessment
This repository contains the solution for the first task of the Incubyte assessment, which is to implement a String Calculator.

The String Calculator is a programming kata designed to practice TDD (Test-Driven Development) and incremental development.

Task Description
The goal was to implement a function stringcalculator(name) that takes a string of numbers and returns their sum, following a set of specific rules that are introduced incrementally.

Features Implemented
The stringcalculator function currently supports the following features:

1.Empty String: Returns 0 for an empty string "".
2.Single Number: Returns the number itself (e.g., "1" returns 1).
3.Two Numbers: Returns the sum of two numbers separated by a comma (e.g., "1,2" returns 3).
4.Any Amount of Numbers: Handles an arbitrary number of numbers separated by commas (e.g., "1,2,3" returns 6).
5.New Lines as Delimiters: Allows new lines as well as commas as delimiters (e.g., "1\n2,3" returns 6).
6.Custom Delimiters: Supports defining a custom delimiter using the format: //[delimiter]\n[numbers].
Example: //;\n1;2 returns 3.
7.Multiple Custom Delimiters (Arbitrary Length): Supports multiple custom delimiters of any length, specified in the format: //[delim1][delim2]...\n[numbers].
Example: //[:::][.][**]\n1:::2.3**4 returns 10.
8.Negative Numbers Handling: Throws an error/prints a message indicating "negative numbers not allowed" if any negative number is passed, listing all negative numbers found. (Note: The current implementation prints the message to the console and returns the sum of non-negative numbers, as demonstrated in the code structure).

Files in this Repository
1.calculator.py: Contains the core implementation of the stringcalculator function.
2.test.test.py: Contains unit tests using Python's unittest module to verify the calculator's functionality.

Prerequisites
  Python 3.x

how to run this file
  in commmand prompt type : python3 test.test.py
