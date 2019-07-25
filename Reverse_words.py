# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    x=[]
    t1=text.split(" ")
    print(t1)
    for i in t1:
        a=i[::-1]
        # print(a)
        x.append(a)
    
    sum=""
    for j in x:
        # print(j)
        sum = sum + j + " "

    # print(sum)

    return sum.strip(" ")

reverse_words("double  spaces")
reverse_words("This is an example!")