# max_gap([13,10,2,9,5]),4
# max_gap([13,3,5]),8
# max_gap([24,299,131,14,26,25]),168
# max_gap([-3,-27,-4,-2]),23
# max_gap([-7,-42,-809,-14,-12]),767
# max_gap([12,-5,-7,0,290]),278
# max_gap([-54,37,0,64,-15,640,0]),576
# max_gap([130,30,50]),80
# max_gap([1,1,1]),0
# max_gap([-1,-1,-1]),0

def max_gap(numbers):
    sort_num=sorted(numbers)
    # print(sort_num)

    x=[]
    
    sum = 0
    for n in range(len(sort_num)):
        sum = sort_num[n] - sort_num[n-1]
        # print(sum)
        x.append(sum)
    
    reverse_x=sorted(x, reverse=True)
    # print(reverse_x[0])
    return reverse_x[0]




max_gap([13,10,2,9,5]),4
max_gap([13,3,5]),8
max_gap([130,30,50]),80
max_gap([1,1,1]),0