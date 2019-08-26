# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# duplicate_count("abcde"), 0
# duplicate_count("abcdea"), 1
# duplicate_count("indivisibility"), 1

def duplicate_count(text):
    text=text.lower()
    x=[]
    for t1 in text:
        if (text.count(t1)) != 1:
            x.append(t1)
    # print(x)
    x=set(x)
    print(len(x))
    return len(x)


duplicate_count("abcde"), 0
duplicate_count("abcdea"), 1
duplicate_count("indivisibility"), 1