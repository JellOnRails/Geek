def reverse_str(str):
    res = ''
    str = str.strip()
    for i in range(len(str)-1, -1, -1):
        res += str[i]
        
    return res
    
    
def print_i(i, n):
    if i <= n:
        print i
        print_i(i+1, n)
        
    return    
    
def print_num(n):
    
    print_i(1, n)
      
import collections

def element(numbers):
    num_list = collections.defaultdict(int)
    
    for i in numbers:
        num_list['i'] += 1
        
    val = 0
    element = ''    
    for key in num_list.keys:
        if val < num_list[key]:
            val = num_list[key]
            element = key
    
    return element      
    
    
    
    
    
    
    
    
    