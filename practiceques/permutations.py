def permutations(string,l,r):
    if l == r:
        print("".join(string))
        return
    else:
        for i in range(l,r+1):
            swap(string,l,i)
            permutations(string,l+1,r)
            swap(string,l,i)

def swap(string,i,j):
    string[i],string[j] = string[j],string[i]
        
a = ['a','b','c']
permutations(a,0,len(a)-1)


    #          ABC   L =0, R =2, I = 0
    #     ABC  BAC  CBA
    # ABC ACB BAC BCA CBA CAB
    