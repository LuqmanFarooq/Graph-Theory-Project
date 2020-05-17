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
**Step 1: Download Python Executable Installer**
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
