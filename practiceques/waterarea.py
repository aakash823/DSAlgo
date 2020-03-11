#O(n) time O(n) space
def waterArea(heights):
    # Write your code here.
	leftmaxes = [0 for i in heights]
	rightmaxes = [0 for i in heights]
	maxes = [0 for i in heights]
	leftmax = 0
	rightmax = 0
	for i in range(len(heights)):
		leftmaxes[i] = leftmax
		leftmax = max(heights[i],leftmax)
	for i in reversed(range(len(heights))):
		rightmax = max(rightmax,heights[i])
		rightmaxes[i] = rightmax
		
	for i in range(len(heights)):
		minheight = min(rightmaxes[i],leftmaxes[i])
		if heights[i] < minheight:
			maxes[i] = minheight - heights[i]
		else:
			maxes[i] = 0
	return sum(maxes)


#O(n) time O(n) space
def waterAreaOptimized(heights):
    # Write your code here.
	maxes = [0 for x in heights]
	leftmax = 0
	for i in range(len(heights)):
		maxes[i] = leftmax
		leftmax = max(leftmax,heights[i])
	rightmax = 0
	for i in reversed(range(len(heights))):
		height = heights[i]
		minheight = min(rightmax,maxes[i])
		if height < minheight:
			maxes[i] = minheight - height
		else:
			maxes[i] = 0
		rightmax = max(rightmax,heights[i])
	return sum(maxes)
			