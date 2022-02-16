'''
Letter case Permutation
Input: "a1B2"
Output: 
a1B2
a1b2
A1B2
A1b2

problem url : https://leetcode.com/problems/letter-case-permutation/
'''

def solve(ip,op):
    if ip == "":
        print(op)
        return
    if ip[0].isdigit():
        op = op + ip[0]
        ip = ip.replace(ip[0],'',1)
        solve(ip,op)
    else:
        op1 = op+ip[0]
        if ip[0].isupper():
            op2 = op+(ip[0]).lower()
        else:
            op2 = op+(ip[0]).upper()
        ip=ip.replace(ip[0],'',1)
        solve(ip,op1)
        solve(ip,op2)

ip = input()
op = ""

solve(ip,op)
