def squareroot(n,p):
    left = 1
    right = n
    ans = 0
    while left <= right:
        mid = (left+right)//2

        if (mid*mid == n):
            return mid
        elif mid*mid < n:
            ans = mid
            left = mid+1
        else:
            right = mid-1
    
    inc = 0.1

    for i in range(p):
        #ans = ans + inc
        while (ans*ans <= n):
            ans +=inc
        ans -= inc
        inc = inc/10
    return ans

print(squareroot(10,3))