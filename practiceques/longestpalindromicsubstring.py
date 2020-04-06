def longestpalindromic(string):
    longest = [0,1]
    for i in range(1,len(string)):
        odd = getlongestfrom(string,i-1,i+1)
        even = getlongestfrom(string,i-1,i)
        if odd[1] - odd[0] > even[1] - even[0]:
            current = odd
        else:
            current = even
        if longest[1] - longest[0] < current[1] - current[0]:
            longest = current
    return string[longest[0]:longest[1]]

def getlongestfrom(string,left,right):
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        left-=1
        right+=1
    return [left+1,right]


print(longestpalindromic("abcdefghfedcbaa"))

