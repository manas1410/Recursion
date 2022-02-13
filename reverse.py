#reverse a list using recursion

def reverse_list(l):
    if len(l) == 1:
        return
    t = l.pop()
    reverse_list(l)
    l.insert(0,t) #appending at 0th index

l = [2,3,4,5]
print(l)
reverse_list(l)
print(l)
