# Muhammad Luqman
# Classes used in Thompson's construction

class State:
    """A State with one or two edges, all edges labeled by label."""
    # Constructor for the Class
    def __init__(self, label=None, edges=None):
        # Every stste has 0,1 or 2 edges from it
        self.edges = edges if edges else []
        # Label for the arrows.None means epsilon.
        self.label = label

class Fragment:
    """An NFA fragment with a start and an accept state."""
    # Constructor
    def __init__(self, start, accept):
        # Start state of the NFA fragment
        self.start = start
        # Accept state of the NFA fragment
        self.accept = accept

def shunt(infix):
    """Return the infix regular expression in postfix."""
    # convert input into stack-ish list
    infix  = list(infix)[::-1]
    
    #operator stack 
    opers, postfix = [], []
    
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
            # get rid of the '('# expected output; "ab|c*."
            opers.pop()
        elif c in prec:
            # push any operators on the opers stack with higher prec to the output.
            while opers and prec[c] < prec[opers[-1]]:
                postfix.append(opers.pop())
            # push c to the operator stack
            opers.append(c)
        else:
            # Typically, we just push the character to the output
            postfix.append(c)

    # pop all operators to the output
    while opers:
        postfix.append(opers.pop())

    # convert output list to string
        return ''.join(postfix)

def compile(infix):
    """Return an NFA Fragment representing the infix regular expression"""
    # Convert infix to postfix
    postfix = shunt(infix)
    # Make postfix a stack of characters.
    postfix = list(postfix)[::-1]
    
    #A stack of NFA fragments
    nfa_stack = []

    while postfix:
        # pop a character from postfix
        c = postfix.pop()
        if c == '.':
            # pop two fragments off the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # point frag2's accept state at frag1's start state
            frag2.accept.edges.append(frag1.start)
            # The new start state is frag2's
            start = frag2.start
            # The new accept state is frag1's
            accept = frag1.accept
        elif c == '|':
            # pop two fragments off the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # create new start and accept states
            accept = State()
            start = State(edges=[frag2.start, frag1.start])
            # point the old accept states at the new one
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)
        elif c == '*':
            # pop a single fragment off the stack
            frag = nfa_stack.pop()
            # create new start and accept states
            accept = State()
            start = State(edges=[frag.start, accept])
            # point the arrows
            frag.accept.edges = [frag.start, accept]
        else:
            accept = State()
            start = State(label=c, edges=[accept])

        # create new instance of Fragment to represent the new NFA
        newfrag = Fragment(start, accept)
        # push the new NFA to the NFA stack
        nfa_stack.append(newfrag)

    # The NFA stack should have exactly one NFA on it.
    return nfa_stack.pop()

# Add a state to a set, and follow all of the e(psilon0 arrows.
def followes(state, current):
    # only do something when we haven't already seen the state.
    if state not in current:
        # put the state itself into current
        current.add(state)
        # see wether state is labelled by e(psilon).
        if state.label is None:
            # loop through the states pointed to by this state.
            for x in state.edges:
                # follow all of their e(psilon)s too.
                followes(x, current)

def match(regex, s):
    # This function will return true if and only if the regular expression
    # regex (fully) matches the string s . it returns false otherwise.

    # compile the regular expressions into an NFA
    nfa = compile(regex)

    # Try to match the regular expression to the string s.
    # the current set of states.
    current = set()
    # Add the first satate,and folow all e(psilon) arrows.
    followes(nfa.start, current)
    # the previous set of states.
    previous = set()

    # Loop through characters in s
    for c in s:
        # keep track of where we were    
        previous = current
        # create a new empty set for states we are about to be in.
        current = set()
        # Lopp through the previous states.
        for state in previous:
            # only follow arrows with not lablled by e(psilon).
            if state.label is not None:
                # if label of the state is equal to the character we have read:
                if state.label == c:
                    # Add the state at the end of the arrow to the current.
                    followes(state.edges[0], current)

    # Ask  the NFA if it matches the string s.
    return nfa.accept in current

if __name__ == "__main__":
    print(match("a.b|b*","bbbbbbbbbbx"))

