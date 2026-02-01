from stack import Stack

def balanced(a_str):
    """
    Check whether a string of brackets is balanced.
    Uses a stack to validate correct order and nesting of brackets.
    :param a_str: String containing bracket characters.
    :return: 'Сбалансированно' if the string is balanced, 'Несбалансированно' otherwise.
    """
    stack = Stack()
    result = 'Сбалансированно'
    for s in a_str:
        if s == '{' or s == '[' or s == '(':
            stack.push(s)
            continue
        if s == '}' or s == ']' or s == ')':
            if stack.is_empty() is True:
                result = 'Несбалансированно'
                break
            the_last = stack.peek()
            if (the_last == '{' and s == '}') or (the_last == '[' and s == ']') or (the_last == '(' and s == ')'):
                stack.pop()
                continue
            else:
                result = 'Несбалансированно'
                break
    if stack.is_empty() is False:
        result = 'Несбалансированно' 
    return result