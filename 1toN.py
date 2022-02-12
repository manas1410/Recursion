#Print 1 to N using Recursion

def print_nos(n):
    if n == 1 :
        print(1)
        return 
    print_nos(n-1)
    print(n)
n = int(input())
print_nos(n)
