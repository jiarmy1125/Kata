# row_sum_odd_numbers(1), 1
# row_sum_odd_numbers(2), 8
# row_sum_odd_numbers(13), 2197
# row_sum_odd_numbers(19), 6859
# row_sum_odd_numbers(41), 68921

def row_sum_odd_numbers(n):
    sum = n*n*n
    print(sum)

    return sum


row_sum_odd_numbers(2)
row_sum_odd_numbers(13)
row_sum_odd_numbers(41)


#              1                 1
#           3     5              8
#        7     9    11           27
#    13    15    17    19        64
# 21    23    25    27    29     125

# 1+3+5+7+9+11
# 1
# 1+3+5  -1
# 1+3+5+7+9+11  -1-3-5
# 1+3+5+7+9+11+13+15+17+19  -1-3-5-7-9-11