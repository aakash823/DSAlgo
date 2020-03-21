def twoNumberSum(array, targetSum):
    # Write your code here.
	nums = {}
	
	for i in range(len(array)):
		potential = targetSum - array[i]
		if potential in nums:
			return [array[i],potential]
		else:
			nums[array[i]] = i
	return []