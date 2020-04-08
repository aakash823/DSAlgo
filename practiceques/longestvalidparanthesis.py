def longestvalidparenthesis(string):
    stack = []
    result = 0
    stack.append(-1)
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack):
                result = max(result,i-stack[-1])
    return result

print(longestvalidparenthesis(")"))