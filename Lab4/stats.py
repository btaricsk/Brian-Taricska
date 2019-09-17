In code, create functions that compute the mean, median, and mode for a list of integers.
Use the following list as a test case: [34, 23, 54, 43, 53, 43, 99, 43, 74, 57, 82, 80, 17]. 
Include the values of mean, median, and mode in README.md.

import math

def mean(alist):
n_num = [34, 23, 54, 43, 53, 43, 99, 43, 74, 57, 82, 80, 17] 

    mean = sum(alist) / len(alist)

>>> mean([34, 23, 54, 43, 53, 43, 99, 43, 74, 57, 82, 80, 17])
    54
  
  return

n = len(n_num) 
n_num.sort() 
  
if n % 2 == 0: 
    median1 = n_num[n//2] 
    median2 = n_num[n//2 - 1] 
    median = (median1 + median2)/2

else: 
    median = n_num[n//2] 
print("Median is: " + str(median))  
 median is 48
  
return

get_mode = dict(data) 
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
  
if len(mode) == n: 
    get_mode = "No mode found"
else: 
    get_mode = "Mode is / are: " + ', '.join(map(str, mode)) 
      
print(get_mode) 

Mode is/are 43

return
