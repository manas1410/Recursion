'''Permutation with Case Change using recursion

Input: ab
Output:
ab
aB
Ab
ABC
'''

def per_wtih_case_change(ip,op):
    if ip == "":
        print(op)
        return
    op1 = op+ip[0]
    op2 = op+(ip[0]).upper()
    ip=ip.replace(ip[0],'',1)
    per_wtih_case_change(ip,op1)
    per_wtih_case_change(ip,op2)

ip = input()
op = ""

per_wtih_case_change(ip,op)
