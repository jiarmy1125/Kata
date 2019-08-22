# remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"), "alpha beta gamma delta")
# remove_duplicate_words("my cat is my cat fat"), "my cat is fat")

def remove_duplicate_words(s):
    s1=s.split(" ")
    # print(s1)

    x=[]
    y=''
    for i in range(len(s1)-1,-1,-1):
        # print(s1[i],i)
        x.append(s1[i])
    # print(x)

    j=0
    while j < len(x):
        if x.count(x[j]) != 1:
            x.remove(x[j])
            j=0
        
        j += 1    
        
    # print(x) 

    for k in range(len(x)-1,-1,-1):
        # print(s1[i],i)
        y += x[k]+' '
    # print(y)

    return y.strip(" ")

# remove_duplicate_words("my cat is my cat fat"), "my cat is fat"
remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta")