def countpalindromesubstring(string):
    result = 0
    for i in range(len(string)):
        odd = getpalindromesubstring(string,i,i)
        even = getpalindromesubstring(string,i-1,i)
        result += odd + even 
    return result


def getpalindromesubstring(string,left,right):
    count = 0
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            return count
        left-=1
        right+=1    
        count+=1
    return count

print(countpalindromesubstring("abc"))