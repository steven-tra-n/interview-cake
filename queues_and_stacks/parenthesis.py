def parenthesis(string, position):
    # 1.  Initialize a stack
    # 2.  Iterate through the string until given position
    # 2a. If encountering a '(', append. Vice versa for ')'
    # 3.  Iterate through the rest until given position
    
    parenthesis_stack = []
    index = position

    # 2.
    # for char in string[:position]:
    #     parenthesis_stack = handle_parenthesis(char, parenthesis_stack)
    #     index += 1
    # 3.

    for char in string[position:]:
        parenthesis_stack = handle_parenthesis(char, parenthesis_stack)

        if len(parenthesis_stack) == 0:
            return index

        index += 1

            
def handle_parenthesis(char, stack):
    if char == '(': # 2a.
            stack.append('(')
    elif char == ')': # 2a.
        if len(stack) == 0:
            raise IndexError('Invalid parenthesis combo')

        stack.pop()

    return stack


input = "((((((((( (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

print(parenthesis(input, 10))