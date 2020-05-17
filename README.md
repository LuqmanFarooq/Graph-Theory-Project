# Graph-Theory-Project
## Description
Program in Python to execute regular expressions on strings using an algorithm known as Thompson’s construction.This program can build a non-deterministic ﬁnite automaton (NFA) from a regular expression, and can use the NFA to check if the regular expression matches any given string of text.
## Implementation
* Shunting yard algorithm to convert a regular expression from infix to postfix.
* Create NFA's for each fragment in the regular expression.
* Macth the infix with a string.
## Running the project
1. Git clone the repository.
2. Change the directory to the project root folder using cd and folder name.
3. Run the program using "python3 runProject.py".
4. Enter infix notation and Press enter.
5. Enter String to match and Press enter.
6. Matched or not Matched message will print on screen depending on the result.
## Research
* Research on infix to postfix conversion
  * research-infixtopostfix.py
  * StateClass.py 
  * testing.py in which i have done unit testing on shunting algorithm and match algorithm.
  * Run research-infixtopostfix.py using python3 research-infixtopostfix.py
  * https://stackoverflow.com/questions/27586287/infix-to-postfix-conversion-in-python

* A Well Written java program to convert regular expressions into NFA using thompsons construction
  * https://github.com/prijatelj/thompson-construction/blob/master/Thompson.java

* Information on Converting Regular Expressions to NFA
  * https://www.geeksforgeeks.org/regular-expression-to-nfa/

* NFA VS DFA
  * https://www.youtube.com/watch?v=FZp7CJwe6nw
* Unit Testing
  * https://docs.python.org/3/library/unittest.html
  * https://www.journaldev.com/15899/python-unittest-unit-test-example
