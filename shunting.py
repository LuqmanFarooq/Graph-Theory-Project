# Muhammad Luqman
# The Shunting Yard Algorithm for the regular expression

# The input.
infix = "(a|b).c*"
print("Input is : ",infix)
# expected output; "ab|c*."
print("Expected: ", "ab|c*.")
# convert input into stack-ish list
infix  = list(infix)[::-1]

#operator stack 
opers = []

#output list.
postfix = []

# operator precedence
prec = {'*':100, '.':80, '|':60, ')':40, '(':20}

# Loop through the input one character at a time
while infix:
  # pop a character  from the input.
  c = infix.pop()

  # Decide what to do based on the character
  if c == '(':
    # push an open bracket to the opers stack
    opers.append(c)
  elif c == ')':
    # pop the operator stack until you find (.
    while opers[-1] != '(':
      postfix.append(opers.pop())
    # get rid of the '('
    opers.pop()
  elif c in prec:
    # push any operators on the opers stack with higher prec to the output.
    while opers and prec[c] < prec[opers[-1]]:
      postfix.append(opers.push())
    # push c to the operator stack
    opers.append(c)
  else:
    # Typically, we just push the character to the output
    postfix.append(c)

# pop all operators to the output
while opers:
  postfix.append(opers.pop())

# convert output list to string
postfix = ''.join(postfix)

# print the result
print("output is: ",postfix)
