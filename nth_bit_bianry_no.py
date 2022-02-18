'''
Print N-bit binary numbers having more 1’s than and equal to 0’s for any prefix
Input: 3
Output:
111
110
101
'''

def solve(o,z,op,n):
    if n==0:
        print(op)
        return
    
    op2 = op 
    op2+='1'
    solve(o+1,z,op2,n-1)
    
    op1 = op
    op1+='0'
    if(o>z):
        solve(o,z+1,op1,n-1)
    
n = int(input())
solve(0,0,"",n)
