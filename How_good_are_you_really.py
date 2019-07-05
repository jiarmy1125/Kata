# better_than_average([2, 3], 5) should return True
# (better_than_average([2, 3], 5), True)

def better_than_average(class_points, your_points):
    sum=0
    for i in class_points:
        sum += i
    sum=sum+your_points
    avg=sum/(len(class_points)+1)

    if (avg < your_points):
        return True
    
    else:
        return False
    

better_than_average([2, 3], 5)
print(better_than_average([2, 3], 1))
print(better_than_average([2, 3], 5))
