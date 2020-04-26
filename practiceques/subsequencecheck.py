def checksubsq(str1,str2):
    i = 0
    j = 0

    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i+=1
            j+=1
        else:
            i+=1
    if j == len(str2):
        return True
    return False

#       i i i i i i
#str1 = c o d i n g
#       j j j j j
#str2 = c o i n

print(checksubsq("coding", "iod"))