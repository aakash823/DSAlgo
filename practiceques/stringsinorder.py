def stringsinorder(firststring,string2):
    i = 0
    j = 0
    while i < len(firststring) and j < len(string2):
        if firststring[i] == string2[j]:
            i+=1
            j+=1
        else:
            i+=1
    if j == len(string2):
        return True
    return False

print(stringsinorder("ab","ba"))