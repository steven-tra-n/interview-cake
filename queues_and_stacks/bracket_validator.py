from ast import Pass


def bracket_validator(input):
    # 1.  Use a stack
    # 2.  Loop through the string
    # 3.  If any open character is encountered, add it to the stack
    # 4.  Closing characters must match the peek 

    closers_stack = []

    for char in input:
        if char == '(' or char == '[' or char == '{':
            closers_stack.append(char)
        elif char == ')':
            if len(closers_stack) == 0 or closers_stack[-1] != '(':
                return False

            if closers_stack[-1] == '(':
                closers_stack.pop()
        elif char == ']':
            if closers_stack[-1] == '[':
                closers_stack.pop()
            else:
                return False
        elif char == '}':
            if closers_stack[-1] == '{':
                closers_stack.pop()
            else:
                return False

    return len(closers_stack) == 0

input = '{ [ ( ] ) }'
print(bracket_validator(input))