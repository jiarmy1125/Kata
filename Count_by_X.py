# count_by(1, 5), [1, 2, 3, 4, 5]
# count_by(2, 5), [2, 4, 6, 8, 10]
# count_by(3, 5), [3, 6, 9, 12, 15]
# count_by(50, 5), [50, 100, 150, 200, 250]
# count_by(100, 5), [100, 200, 300, 400, 500]

def count_by(x, n):
    sum=0
    a=[]
    for i in range(1,n+1):
        sum = x*i
        a.append(sum)
        # print(sum)
    # print(a)
    return a


count_by(1, 5)
count_by(3, 5)