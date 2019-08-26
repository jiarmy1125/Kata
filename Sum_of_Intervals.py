# sumIntervals( [[1,2],[6, 10],[11, 15]] ); // => 9
# sumIntervals( [[1,4],[7, 10],[3, 5]] ); // => 7
# sum_of_intervals([(1, 5)]), 4
# sum_of_intervals([(1, 5), (6, 10)]), 8
# sum_of_intervals([(1, 5), (1, 5)]), 4
# sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7

def sum_of_intervals(intervals):
    
    x=[]

    for tu in intervals:
        for i in range(tu[0],tu[1]):
            x.append(i)
    
    # print(x)

    x=set(x)    
    # print(x)
    total=len(x)
    print(total)
    return total

sum_of_intervals([(1, 5)]) ,4
sum_of_intervals([(1, 5), (6, 10)]), 8    
sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7


