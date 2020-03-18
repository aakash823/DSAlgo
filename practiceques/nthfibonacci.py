def getNthFib(n):
    # Write your code here.
	if n == 1 or n == 0:
		return 0
	if n == 2:
		return 1
	
	first = 0
	second = 1
	
	for i in range(n-2):
		third = first+second
		first = second
		second = third
	return third