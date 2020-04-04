def checkanagrams(string1,string2):
    array1 = [0 for i in range(26)]

    
    for i in range(len(string1)):
        array1[ord(string1[i])-97] +=1
        array1[ord(string2[i])-97] -=1

    for i in range(len(array1)):
        if array1[i] != 0:
            return False
    return True



def sortstring(string):
    return "".join(sorted(string))


print(sortstring("bbansdwr"))
print(checkanagrams("abc","bac"))