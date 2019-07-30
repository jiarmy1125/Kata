# ls = [0, 1, 3, 6, 10]
# ls = [1, 3, 6, 10]
# ls = [3, 6, 10]
# ls = [6, 10]
# ls = [10]
# ls = []
# [20, 20, 19, 16, 10, 0]

def parts_sums(ls):
    y=[]
    ls.append(0)
    ls_1=ls[::-1]
    # print(ls_1)

    sum=0
    for i in range(len(ls_1)):
        # print(ls_1[i])
        sum += ls_1[i]
        # print(sum)
        y.append(sum)
        # y.pop(0)
    y=y[::-1]
    print(y)
    return y

# def parts_sums(ls):
#     y=[]
#     for i in range(len(ls)):
#         for j in range(len(ls)):
#             print(ls)
#             sum = 0
#             for k in ls:
#                 sum+=k
#             y.append(sum)
#             ls.pop(0)
#     y.append(0)
#     # print(ls)
#     print(y)
#     return y
    

parts_sums([0, 1, 3, 6, 10])

# def parts_sums(ls):
#     # your code
#     sums = []
#     k = len(ls)
#     ls += [0]
#     for i in range(k+1):
#         sum = 0
#         for j in ls:
#             sum += j
#         sums.append(sum)
#         del ls[0]
#     return sums

# for i in range(5):
#     # x.pop(0)
#     print(x)
#     sum = 0
#     for k in x:
#         sum+=k
#         # print(sum)
#     y.append(sum)
#     x.pop(0)

# print(x)
# print(y)

