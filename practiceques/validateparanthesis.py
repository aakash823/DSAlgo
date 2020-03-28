def balancedBrackets(string):

	closing = '}])'
	opening = '[{('
	matching = {
		')': '(',
		'}': '{',
		']': '['
	}
	stack = []
	
	for i in range(len(string)):
		if string[i] in opening:
			stack.append(string[i])
		else:
			if len(stack) == 0:
				return False
			elif stack[-1] == matching[string[i]]:
				stack.pop()
			else:
				return False
	return len(stack)==0