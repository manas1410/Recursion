#print subsets using recursion
#example for "ab":" ","a","b","ab"

lst = []
def solve(ip,op):
    if ip=="":
        lst.append(op)
        return
    op1 = op 
    op2 = op 
    op2+=ip[0]
    ip = ip.replace(ip[0],'',1)
    solve(ip,op1)
    solve(ip,op2)
ip=input()
op = ""
solve(ip,op)
print(",".join(lst))
