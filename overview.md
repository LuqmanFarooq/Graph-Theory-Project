# Introduction
Python program that can build a non-deterministic ﬁnite automaton (NFA) from a regular expression and can use the NFA to check if the regular expression matches any given string of text. The program from scratch and doesn’t use the re package from the Python standard library nor any other external library. A regular expression is a string containing a series of characters, some of which may have a special meaning. For example, the three characters., |, and* have the special meanings concatenate, or, and Kleene star respectively. For example, the regular expression 0.1 means a 0 followed by a 1, 0|1 means a 0 or a 1, and 1* means any number of 1’s. These special characters must be used in your submission. Other special characters you might consider allowing a sinuate bracket () which can be used for grouping, + which means at least one of, and which means zero or one of. You might also decide to remove the concatenation character, so that 1.0 becomes 10, with the concatenation implicit. You may initially restrict the non-special characters your program works with to 0 and 1. However, you should at least attempt to expand these to all the digits, and the characters a to z, and A to Z.

The repository contains hello.c, hello.py, myScript.py, regex.py, shunting.py, testing.py, runProject.py, research-infixtopostfix.py, StackClass.py

**hello.c** = contains sample program written in c language.

**hello.py** = contains a program written in python programming language which is the same sample program which was written in c language in hello.c

**Shunting.py** = contains the shunting yard algorithm which take in an infix expression and converts it into postfix expression.

**regex.py** = contains all the functions for converting infix to postfix, creating NFA fragments and then comparing.

**myScript.py** = contains list of tests which are performed on match function.

**testing.py** = contains a list of unit tests for testing shunt function and compare function of regex.

**runProject.py** = contains the code for running the project.it takes in an infix expression and converts it to postfix and takes in string to match with the postfix expression and displays the result.

**research-infixtopostfix.py** = contains code to convert infix to postfix by own research.

**StackClass.py** = contains functions used in research-infixtopostfix.py.

# How to Run the project
### Prerequisites
* A system running Windows 10 with admin privileges
* Command Prompt (comes with Windows by default)
### Python 3 Installation on Windows
### Step 1: Download Python Executable Installer
1. Open your web browser and navigate to the Downloads for Windows section of the official Python website.
2. Search for your desired version of Python3.
3. Select a link to download either the Windows x86-64 executable installer or Windows x86 executable installer. The download is approximately 25MB.
### Step 2: Run Executable Installer
1. Run the Python Installer once downloaded.
2. Make sure you select the Install launcher for all users and Add Python 3.7 to PATH checkboxes. The latter places the interpreter in the execution path. For older versions of Python that do not support the Add Python to Path checkbox, see Step 6.
3. Select Install Now – the recommended installation options.
4. The next dialog will prompt you to select whether to Disable path length limit. Choosing this option will allow Python to bypass the 260-character MAX_PATH limit. Effectively, it will enable Python to use long path names.
### Step 3: Verify Python Was Installed On Windows
1. Navigate to the directory in which Python was installed on the system. In our case, it will be C:\Users\Username\AppData\Local\Programs\Python\Python37 since we have installed the latest version.
2. Double-click python.exe.
### Step 4: Verify Pip Was Installed
If you opted to install an older version of Python, it is possible that it did not come with Pip preinstalled. Pip is a powerful package management system for Python software packages. Thus, make sure that you have it installed.

We recommend using Pip for most Python packages, especially when working in virtual environments.

To verify whether Pip was installed:

1. Open the Start menu and type “cmd.”
2. Select the Command Prompt application.
3. Enter pip -V in the console. If Pip was installed successfully, you should see the pip version
Pip has not been installed yet if you get the following output:

’pip’ is not recognized as an internal or external command,
Operable program or batch file.
If your version of Python is missing Pip, see our article How to Install Pip to Manage Python Packages on Windows.

### Step 5: Add Python Path to Environment Variables (Optional)
We recommend you go through this step if your version of the Python installer does not include the Add Python to PATH checkbox or if you have not selected that option.

Setting up the Python path to system variables alleviates the need for using full paths. It instructs Windows to look through all the PATH folders for “python” and find the install folder that contains the python.exe file.

1. Open the Start menu and start the Run app.
2. Type sysdm.cpl and click OK. This opens the System Properties window.

3. Navigate to the Advanced tab and select Environment Variables.

4. Under System Variables, find and select the Path variable.

5. Click Edit.

6. Select the Variable value field. Add the path to the python.exe file preceded with a semicolon (;). For example, in the image below, we have added “;C:\Python34.”
7. Click OK and close all windows.

By setting this up, you can execute Python scripts like this: Python script.py

Instead of this: C:/Python34/Python script.py

As you can see, it is cleaner and more manageable.

## Running the Project
1. open cmd in the folder where you want to save the project.and in cmd type git clone https://github.com/LuqmanFarooq/Graph-Theory-Project.
2. Change the directory to the project root folder using cd and folder name e.g "cd Graph-Theory-project".
3. Run the program using "python3 runProject.py" or "python runProject.py" in cmd.
4. Enter infix notation and Press enter.
5. Enter String to match and Press enter.

Matched or not Matched message will print on screen depending on the result.
# Test
## Unit Testing
Run the testing file named as testing.py using "python3 testing.py" or "python testing.py" in cmd.

it uses the assert function of the python to unit test the function shunt of shunting algorithm and and the function match with a lists of tests.

## General Testing
Run the testing file name myScripts.py  using "python3 myScripts.py" or "python myScripts.py" in cmd.

it uses the assert function of the python to do a list of tests wirtten in the file to match expressions and strings.

# Algorithms Used

## Shunting Yard Algorithm
### What is the Shunting-Yard Algorithm?
This algorithm is an operator-precedence parser that is specifically designed to parse mathematical expressions into postfix notation for computation. Postfix notation (Reverse Polish notation) is a mathematical notation in which the operators follow the numbers.

For example, 4 + 5 will turn into 4 5 +

Postfix notation removes the need for parentheses and allows computer programs to read in mathematical expressions one symbol after the other, instead of worrying about operator precedence and parentheses during computation.

### how to convert a regular expression into postfix notation.
#### What is our regular expression?
The regular expression we will be using will be: a(a+b)*b

This expression will accept all strings that begin with the letter ‘a’ and end in the letter ‘b.’
#### Establish operator precedence
Before we can begin converting our expression to postfix notation, we must establish the operator precedence. Knowing the precedence will be necessary during the conversion when we push operators onto the stack. We will need to know which operator has higher precedence in order to decide the correct action to take.

The precedence from highest to lowest is:
1. Closure (Kleene star) a*
2. Concatenation ab
3. Union a+b
#### Explicitly inserting a concatenation symbol
The concatenation expression usually does not have a symbol between the two letters ab. This will make our computation more difficult than necessary when we do the conversion. So, in order to easily handle this I will be using an ? symbol between the two letters for every concatenation.
So, ab will now turn into a?b
If we apply this change to our regular expression, we will now get: a?(a+b)*?b
#### Basic Rules of the Algorithm
* If the input symbol is a letter… append it directly to the output queue.
* If the input symbol is an operator… if there exists an operator already on the top of the operator stack with higher or equal precedence than our current input symbol, remove the operator from the top of the operator stack and append it to the output queue. Do this until the current input symbol has a higher precedence than the symbol on the top of the operator stack, or the operator stack is empty.
* If the input symbol is an operator AND there is a left parenthesis on top of the stack… push the input symbol onto the stack on top of the left parenthesis.
* If the input symbol is an ( … append it to the operator stack.
* If the input symbol is an ) … pop all operators from the operator stack and append them to the output queue until you find an ( . Then, you can remove both of those parentheses and continue with the algorithm.
#### Diagram
![Shunting Diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Shunting_yard.svg/800px-Shunting_yard.svg.png)
## Postfix to NFA Conversion using Thompson's Construction.
The algorithm that makes this possible, is known as Thompsons Construction. It gives the idea of breaking an expression into a collection of small NFA's, one for each character in the expression, which will be combined to provide a diagram of one large NFA which will then be used to check if a string matches the expression.

The procedure used is as follows:

* Expressions are parsed left to right.
* Each character that is read in, has an NFA built for it.
* The NFA will require an initial state and an accept state.
* Each NFA is added to a stack where all the letters' NFA's will exist.
* When a special character is read, the NFA's on the stack will then be removed. It can be 1 or 2, dependent on the type of special character.
* The NFA's will then be joined to create a bigger NFA which is then added to the stack.
* Adding each individual NFA to the stack everytime.
## Matching Algorithm
This function will return true if and only if the regular expression regex (fully) matches the string s . it returns false otherwise.
### Steps for matching
* compile the regular expressions into an NFA.
* Try to match the regular expression to the string s.the current set of states.
* Add the first satate,and folow all e(psilon) arrows.
* Loop through characters in s.
* keep track of where we were.
* create a new empty set for states we are about to be in.
* Lopp through the previous states.
* only follow arrows with not lablled by e(psilon).
* if label of the state is equal to the character we have read:Add the state at the end of the arrow to the current.
* Ask  the NFA if it matches the string s.
## Command Line Interface Arguments
Python also has a module called argparse in the standard library for parsing command-line arguments.
# Refrences
* https://medium.com/@gregorycernera/converting-regular-expressions-to-postfix-notation-with-the-shunting-yard-algorithm-63d22ea1cf88
* https://stackoverflow.com/questions/27586287/infix-to-postfix-conversion-in-python
* https://github.com/prijatelj/thompson-construction/blob/master/Thompson.java
* https://www.geeksforgeeks.org/regular-expression-to-nfa/
* https://www.youtube.com/watch?v=FZp7CJwe6nw
* https://github.com/michellelally/Graph-Theory-Project/wiki/Postfix-to-NFA-Conversion-Algorithm
* https://www.youtube.com/watch?v=QILBGC7TApM
* https://docs.python.org/3/library/unittest.html
* https://www.journaldev.com/15899/python-unittest-unit-test-example
