# score(  [2, 3, 4, 6, 2] ), 0
# score(  [4, 4, 4, 3, 3] ), 400
# score(  [2, 4, 4, 5, 4] ), 450

def score(dice):
    x=[]
    sum=0

    for i in range(1,7):
        # print(i,dice.count(i))
        x.append(dice.count(i))
    # print(x)

    for x1 in range(len(x)):  #個數1,2,3,4,5
        print(x1+1,x[x1])
        if x[x1] > 3:         #處理個數4,5
            if x[x1]-1==3:    #4
                if (x1+1)==1:
                    sum += (1000+100)
                elif (x1+1)==2:
                    sum += (200)
                elif (x1+1)==3:
                    sum += (300)
                elif (x1+1)==4:
                    sum += (400)
                elif (x1+1)==5:
                    sum += (500+50)
                elif (x1+1)==6:
                    sum += (600)
                
            elif x[x1]-2 ==3: #5
                if (x1+1)==1:
                    sum += (1000)
                elif (x1+1)==2:
                    sum += (200)
                elif (x1+1)==3:
                    sum += (300)
                elif (x1+1)==4:
                    sum += (400)
                elif (x1+1)==5:
                    sum += (500)
                elif (x1+1)==6:
                    sum += (600)

        elif x[x1] < 3:        #處理個數1,2
            if x[x1]+1==3:
                if (x1+1)==1:
                    sum += (100*2)
                elif (x1+1)==5:
                    sum += (50*2)
            elif x[x1]==1:
                if (x1+1)==1:
                    sum += (100)
                elif (x1+1)==5:
                    sum += (50)
        
        elif x[x1]==3:        #處理個數3
            if (x1+1)==1:
                sum += (1000)
            elif (x1+1)==2:
                sum += (200)
            elif (x1+1)==3:
                sum += (300)
            elif (x1+1)==4:
                sum += (400)
            elif (x1+1)==5:
                sum += (500)
            elif (x1+1)==6:
                sum += (600)

    return sum


print(score(  [2,2,2,2,6] ))

#  Three 1's => 1000 points--------------
#  Three 6's =>  600 points--------------
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points-----------
#  One   5   =>   50 point