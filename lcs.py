'''
problem url - https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
'''
def lcs(x,y,n,m):
    if n==0 or m==0:
        return 0
    if x[n-1] == y[m-1]:
        return 1+lcs(x,y,n-1,m-1)
    else:
        return max(lcs(x,y,n,m-1),lcs(x,y,n-1,m))
        
    
x=input()
y=input()
l=0
print(lcs(x,y,len(x),len(y)))
    
