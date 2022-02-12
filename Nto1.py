#Print Numbers from N to 1 using Recursion

def print_nos(n):
    if n == 1 :
        print(1)
        return 
    print(n)
    print_nos(n-1)
    
n = int(input())
print_nos(n)
