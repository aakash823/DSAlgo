def printprimes(n):

    print("2 ",end = '')
    for i in range(3,n+1):
        flag = 0
        for j in range(2,i//2+1):
            if i%j == 0:
                flag = 1
                break
        if flag == 0:
            print("{} ".format(i),end = '')

#printprimes(50)


def power(x,n):
    ans = 1
    i=1
    while i <=n:
        ans = ans*x
        i+=1
    return ans


def powerrecursive(x,n):
    # if n==1:
    #     return x
    # return x*powerrecursive(x,n-1)
    return x*powerrecursive(x,n-1) if n > 1 else x



def printallsubstrings(string):
    substring = list(string)
    length = 0
    maxlenght = 0
    biggest = ""
    for i in range(len(string)):
        for j in range(i,len(string)):
            k = i
            current = "".join(substring[k:j+1])
            length = j-k+1
            if ispalindrome(current):
                if length > maxlenght:
                    biggest = current
                    maxlenght = length
    return biggest


def ispalindrome(current):
    i = 0
    j = len(current)-1
    while i < j:
        if current[i] != current[j]:
            return False
        i+=1
        j-=1
    return True    



#print()
print(power(3,3))
print(powerrecursive(3,3))
print(printallsubstrings("abcbaaabbb"))