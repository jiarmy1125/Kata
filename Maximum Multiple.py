# max_multiple(2,7),6
# max_multiple(3,10),9

def max_multiple(divisor, bound):
    # sum = 0
    # for i in range(bound):
    #     sum = divisor*i
    #     if sum == bound:
    #         print(bound)
        
    #     if sum < bound:

    mod = bound % divisor

    if mod ==0:
        print(bound)
    
    else:
        print(bound-mod)



max_multiple(2,8)
max_multiple(3,10)
