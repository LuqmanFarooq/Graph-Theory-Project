# Muhammad Luqman
# G00353385

"""This is the script that is used to the run the program.
It has menu for the user and prompts for the user to enter their own infix notations and the string to match"""

# importing the regex.py file which includes all the methods and algorithms
import regex
# importing argparse library for command line arguments
import argparse

# creating the parser
parser = argparse.ArgumentParser(usage="Help - Instruction to test the program")

# Add the arguments
parser.add_argument('infixexpression', help="Enter infix expression e.g (a.b|b*)")

parser.add_argument('String', help="Eter a string to match  e.g (bbbbbb)")

# parse the arguments
args = parser.parse_args()

# Printing Header on the Screen
print("-----------------------Muhammad Luqman------------------G00353385----------------Graph Theory Project------------------------")

# prompt user to enter infix notation to match
u_infix = input("Please enter an infix :")

# validation if user leaves infix empty
while u_infix == "":
    print("Cannot be Empty!")
    # prompt user to enter infix notation to match
    u_infix = input("Please enter an infix :")
    
# Prompt user to enter the string to match
string  = input("please enter a string :")

# validation if user leaves string empty
while string == "":
    print("Cannot be Empty!")
    # Prompt user to enter the string to match
    string  = input("please enter a string :")
    
# if the result is True then it prints the following statement
if(regex.match(u_infix,string)) == True:
    print("The inputs Matched!")
    
# if the result is False then it prints the following statement
elif(regex.match(u_infix,string)) == False:
    print("The inputs not Matched")
