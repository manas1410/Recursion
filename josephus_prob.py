''' 
Josephus Problem | Game of Death in a circle | Execution in Circle
Input: 40 7
Output: 24
problem url : https://practice.geeksforgeeks.org/problems/game-of-death-in-a-circle1840/1#
'''

# cook your dish here
cur = 0
def solve(l,k):
    global cur
    if len(l)==1:
        return
    kill = (cur+k-1)%len(l)
    del(l[kill])
    cur = kill
    solve(l,k)
    
n,k=map(int,input().split())
l = [i+1 for i in range(n)]
solve(l,k)
print(l[0])

'''
or anothe easy solution 
'''

def safePos(self, n, k):
    # code here 
    l = [i+1 for i in range(n)]
    cur = 0
    while(len(l)>1):
        cur = (cur+k-1)%len(l)
        del[l[cur]]
    return l[0]
