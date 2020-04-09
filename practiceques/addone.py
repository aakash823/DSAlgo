def addone(array):
    if array[len(array)-1] == 9:
        carry = 1
        for i in range(len(array)-1,0,-1):
            if array[i] + carry == 10:
                carry = 1
                array[i] = 0
            else:
                array[i] += carry
                carry = 0
        if array[0] + carry == 10:
            array.append(1)
            array[0] = 0
            for i in range(len(array)-1,0,-1):
                array[i] = array[i-1]
            array[0] = carry
    else:
        array[len(array)-1] +=1
    return array



print(addone([9,9,9,9,9]))    