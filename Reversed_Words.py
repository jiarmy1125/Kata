# reverseWords("hello world!"), "world! hello"

# def reverseWords(str):
#     x=str.split(" ")
#     print(x)
    
#     sort=sorted(x,reverse=True)  # sorted 按照ASCII排列 ABC>abc
#     print(sort)

#     sort_1=''

#     for i in range(len(sort)):
#         sort_1 += sort[i] + " "
    
#     return sort_1.strip(" ")

def reverseWords(str):
    x=str.split(" ")
    
    b=x[::-1]

    sort_1=''

    for i in range(len(b)):
        sort_1 += b[i] + " "
    
    return sort_1.strip(" ")

print(reverseWords("yoda this speak like doesn't"))
print(reverseWords("hello world!"))