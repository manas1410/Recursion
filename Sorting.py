#sorting an array using recursion

def insert_func(n,temp):
    if len(n)==0 or n[-1]<=temp:
        n.append(temp)
        return
    val = n[-1]
    n.pop()
    insert_func(n,temp)
    n.append(val)
def sort_func(n):
    if len(n) == 1:
        return
    temp = n[-1]
    n.pop()
    sort_func(n)
    insert_func(n,temp)

lst = [1,10,5,7,4]
print(lst)
sort_func(lst)
print(lst)

