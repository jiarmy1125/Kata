# my_gloves = ["red","green","red","blue","blue"]
# number_of_pairs(my_gloves) == 2;// red and blue

# red_gloves = ["red","red","red","red","red","red"];
# number_of_pairs(red_gloves) == 3; // 3 red pairs

# number_of_pairs(["red","red"]),1
# number_of_pairs(["red","green","blue"]),0
# number_of_pairs(["gray","black","purple","purple","gray","black"]),3
# number_of_pairs([]),0
# number_of_pairs(["red","green","blue","blue","red","green","red","red","red"]),4

def number_of_pairs(gloves):
    x=[]
    g2=0
    
    for g1 in gloves:
        print(g1,gloves.count(g1))
        if (gloves.count(g1))%2 == 0:
            # print(g1,gloves.count(g1))
            g3=gloves.count(g1)//2
            x.append(g1)
            if g3 != 1:
                for k in range(0,g3,2):
                    k=str(k)
                    x.append(g1+k)

        else:
            g2=(gloves.count(g1))//2
            print(g1," ",g2)
            if g2 !=0:
                for k in range(g2):
                    k=str(k)
                    x.append(g1+k)
            
            


    # print(x)
    x=set(x)
    print(x)


    print(len(x))
    return len(x)





# number_of_pairs(["red","red"]),1
# number_of_pairs(["gray","black","purple","purple","gray","black"]),3
# number_of_pairs([]),0
number_of_pairs( ['Silver', 'White', 'Teal', 'White', 'Black', 'Olive', 'Navy', 'Red', 'Olive', 'Red', 'Red', 'Silver', 'Maroon', 'Black', 'Yellow', 'Red', 'Yellow'])
7