def mostfrequant(array):
    # array.sort()
    # max1 = 0
    # key = 0
    # for i in range(len(array)-1):
    #     count = 0 
    #     while array[i] == array[i+1]:
    #         count+=1
    #         i+=1
    #     if count > max1:
    #         max1 = count
    #         key = array[i]
    # return key
    hashtable = {}

    for element in array:
        if element in hashtable:
            hashtable[element] += 1
        else:
            hashtable[element] = 1
    
    max1 = 0
    key1 = 0
    for key,value in hashtable.items():
        if value > max1:
            max1 = value
            key1 = key
    return key1


print(mostfrequant([1,2,3,1,1,4,2,2,3,3]))