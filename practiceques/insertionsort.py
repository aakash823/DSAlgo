def insertionsort(array):

    for i in range(1,len(array)):
        j = i
        while j>0:
            if array[j] < array[j-1]:
                swap(j,j-1,array)
            j-=1
    return array

def swap(i,j,array):
    array[i],array[j] = array[j], array[i]

print(insertionsort([5,4,19,12,-7,16,25,3]))