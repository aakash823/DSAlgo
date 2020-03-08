class Rangequery:
    def __init__(self):
        self.cache = []
    
    def rangebuild(self,array):
        self.cache = [0 for i in range(len(array)+1)]

        for i in range(len(self.cache)-1):
            self.cache[i+1] = self.cache[i] + array[i]
        #return self.cache

    def getquery(self,i,j):
        
        return self.cache[j] - self.cache[i-1]
obj = Rangequery()
obj.rangebuild([1,2,3])
print(obj.getquery(1,3))