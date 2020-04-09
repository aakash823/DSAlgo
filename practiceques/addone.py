def addone(array):
    carry = 0
    k = len(array) - 1 
    array[k] += 1
    if array[k] == 10:
        carry = 1
        array[k] = 0
    for i in range(k-1,0,-1):
        if array[i] + carry == 10:
            carry = 1
            array[i] = 0
        else:
            array[i] += carry
            carry = 0
    if array[0] + carry == 10:
        array[0] = 0
        array.append(1)
        for i in range(k+1,0,-1):
            array[i] = array[i-1]
        array[0] = 1


    return array
print(addone([1,3,4]))    