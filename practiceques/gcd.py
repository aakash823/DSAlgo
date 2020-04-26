def printgcd(a,b):
    if a%b == 0:
        return b
    return printgcd(b,a%b)


print(printgcd(10,15))




#   8|  20  | 2
#       16
#        4 | 8 | 2
#            8
#            0 
#
#
#
###
#
#