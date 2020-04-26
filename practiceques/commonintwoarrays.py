def commonintwoarrays(array1,array2):
    #O(M+N)
    #O(M)
    common = []
    hashtable = {}
    for i in range(len(array1)):
        hashtable[array1[i]] = True
    
    for i in range(len(array2)):
        if not array2[i] in hashtable:
            common.append(array2[i])
    return common


print(commonintwoarrays([1,3,4,7,9], [1,2,4,5,9,10]))