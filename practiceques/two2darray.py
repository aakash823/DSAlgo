
def arr():
    # edits = [[x for x in range(5)] for y in range(4)]
    # for i in range(1,4):
    #     edits[i][0] = 1+edits[i-1][0]
    # return edits

    array1 = [1,2,3,4,5]
    array2 = array1
    array2[2] = 5
    array2[0] = 7
    return array1
print(arr())