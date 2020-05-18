
# Muhammad Luqman
# G00353385

"""This is the script that is used to the run the program.
It has menu for the user and prompts for the user to enter their own infix notations and the string to match"""

# importing the regex.py file which includes all the methods and algorithms
import regex
# importing argparse library for command line arguments
import argparse

# creating the parser
parser = argparse.ArgumentParser(usage="Help - Instruction to test the program",epilog="Enter infix E.g (a.b) and Enter string E.g ab")

#Add the parameters positional/optional
parser.add_argument('-i','--infix', help="Infix notation e.g a.b")
parser.add_argument('-s','--stringMatch', help="Infix notation e.g ab")
# parse the arguments
args = parser.parse_args()

# if the result is True then it prints the following statement
if(regex.match(str(args.infix),str(args.stringMatch))) == True:
    print("The inputs Matched!")
    
# if the result is False then it prints the following statement
elif(regex.match(str(args.infix),str(args.stringMatch))) == False:
    print("The inputs not Matched")
