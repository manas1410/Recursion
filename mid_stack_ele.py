#delete middle element from the stack using recursion

def mid_stake(l,k):
    if  k==1 :
        l.pop()
        return 
    temp  = l[-1]
    l.pop()
    mid_stake(l,k-1)
    l.append(temp)

l = [1,2,3,4,5]
mid_stake(l,3)
print(l)
    
