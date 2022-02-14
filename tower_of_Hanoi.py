#Tower of Hanoi using recursion
#problem url https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

u = 0
def solve(n,source,destination,helper):
    global u 
    u+=1 
    if n==1:
        print(n,"from",source, "to", destination)
        return 
    solve(n-1,source,helper,destination)
    print(n,"from",source, "to", destination)
    solve(n-1,helper,destination,source)
n=4
solve(n,"A","B","C")
print("Nos. of steps:",u)
