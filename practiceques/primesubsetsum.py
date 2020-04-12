import numpy as np 
  
maxN = 20
maxSum = 50
minSum = 50
base = 50
  
# To store the states of DP  
dp = np.zeros((maxN, maxSum + minSum));  
v = np.zeros((maxN, maxSum + minSum));  
  
# Function to return the required count  
def findCnt(arr, i, required_sum, n) : 
  
    # Base case  
    if (i == n) : 
        if (required_sum == 0) : 
            return 1;  
        else : 
            return 0;  
  
    # If the state has been solved before  
    # return the value of the state  
    if (v[i][required_sum + base]) : 
        return dp[i][required_sum + base];  
  
    # Setting the state as solved  
    v[i][required_sum + base] = 1;  
  
    # Recurrence relation  
    dp[i][required_sum + base] = findCnt(arr, i + 1,required_sum, n) +  findCnt(arr, i + 1, required_sum - arr[i], n);  
      
    return int(dp[i][required_sum + base]);  
  
# Driver code  
if __name__ == "__main__" :  
  
    arr = [ 2,3,5,7 ];  
    n = len(arr);  
    x = 5;  
  
    print(findCnt(arr, 0, x, n))