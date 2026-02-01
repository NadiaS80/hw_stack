from stack import Stack

def balanced(a_str):
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