# max_product([0]*10, 5), 0
# max_product([4,3,5], 2), 20
# max_product([10,8,7,9], 3), 720
# max_product([8,6,4,6], 3), 288


def max_product(lst, n_largest_elements):
    lst = sorted(lst,reverse=True)
    print(lst)

    sum=1
    
    for i in range(n_largest_elements):
        sum = sum * lst[i]


    print(sum)
    return sum
    





max_product([10,8,7,9],3)
max_product(list(range(10, -1, -1)), 5)


# maxProduct ({8, 10 , 9, 7}, 3) ==>  return (720) 
# 8 * 9 * 10 = 720