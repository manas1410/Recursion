#Permutation with Spaces using recursion
''' Input: ABC , Output: ABC,A_B_C,A_BC,AB_C
url = https://www.youtube.com/watch?v=1cspuQ6qHW0&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY'''

def per_wtih_space(ip,op):
    if ip == "":
        print(op)
        return
    op1 = op+ip[0]
    op2 = op
    op2+='_'+ip[0]
    ip=ip.replace(ip[0],'',1)
    per_wtih_space(ip,op1)
    per_wtih_space(ip,op2)

ip = input()
op = ""
op+=ip[0]

per_wtih_space(ip[1::],op)
