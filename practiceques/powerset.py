#Printing all the subsets of an array
#{1,2,3} = {},{1},{2},{3},{1,2},{2,3},{1,3},{1,2,3}
#T(n) = O(n*2^n) | S(n) =  O(n*2^n)

def powerset(array):
	subsets = [[]]
	for elements in array:
		for i in range(len(subsets)):
			subsets.append(subsets[i] +[elements])
	return subsets
