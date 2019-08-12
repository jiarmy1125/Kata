# minimum_steps([4,6,3], 7), 1)
# minimum_steps([10,9,9,8], 17), 1)
# minimum_steps([8,9,10,4,2], 23), 3)
# minimum_steps([19,98,69,28,75,45,17,98,67], 464), 8)
# minimum_steps([4,6,3], 2), 0)

def minimum_steps(numbers, value):
    sort_num=sorted(numbers)
    # print(sort_num)

    sum = 0
    x=0 
    for n in range(len(sort_num)):
        sum += sort_num[n]
        if sum >= value:
            # print(n,sort_num[n],sum)
            x += n
            break

    print(x)
    return x
    

minimum_steps([1, 10, 12, 9, 2, 3], 6), 2
minimum_steps([4,6,3], 2), 0
minimum_steps([19,98,69,28,75,45,17,98,67], 464), 8