# find_outlier([2, 4, 6, 8, 10, 3]), 3
# find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11
# find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160

def find_outlier(integers):
    even=[]
    odd=[]
    for i in integers:
        if (i%2) == 0:
            even.append(i)
        
        else:
            odd.append(i)
    
    if len(odd) == 1:
        return odd[0]
    
    elif len(even) == 1:
        return even[0]

print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])) 
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))