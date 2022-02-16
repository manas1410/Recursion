'''
Generate all Balanced Parentheses using recursion
Input: 3
Output: ((())),(()()),(())(),()(()),()()()
'''

answer = []
def solve(openn,closen,op):
    if openn == 0 and closen == 0:
        answer.append(op)
        return
    if openn!=0:
        op1 = op + '('
        solve(openn-1,closen,op1)
    if closen>openn:
        op2 = op + ')'
        solve(openn,closen-1,op2)
n = int(input())
openn,closen = n,n 
op = ""
solve(openn,closen,op)
print(','.join(answer))
