#Unit Testing  

import unittest
from regex import shunt
from regex import match

#Unittest is a library of python   
class Testing(unittest.TestCase):
    #This function tests the function 'shunt()' which is defined in regex.py
    #and takes a infix regular expression and convert to a postfix one
    def testShunt(self):
        postfix = shunt("(a|b).c*")
        print(f"\nConverting (a*|b*).(c|b) to postfix: {postfix}" )
        #assertEqual() function takes two parameters and compare if they are equals
        self.assertEqual(postfix, "ab|c*")

    #This function runs a list of tests to test the function 'match()' which is defined in regex.py
    #which takes a regular expression and matchs with the entered string and givs the result
    def testRegexMatch(self):
        tests = [
            ["a.b|b*", "bbbbbb", True],
            ["a.b|b*", "bbx", False],
            ["a.b", "ab", True],
            ["b**","b",True],
            ["b*", "",True],
            ["a.b?.a*", "abba", False],
            ["a.b?.a*", "abaaa", True],
            ["a.b+.a*", "aa", False],
            ["a.b+.a*", "abbba", True],
            ["a.b|b*", "bbbxb", False],
            ["a.b", "ab", True]
        ]
        for test in tests:
            print(f"The result of matching '{test[0]}' with '{test[1]}' is = {test[2]}")
            self.assertEqual(match(test[0],test[1]), test[2])
# it will only run if its the main class
if __name__ == '__main__':
    unittest.main()
