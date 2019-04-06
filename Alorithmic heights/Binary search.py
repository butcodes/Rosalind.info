#binary search

def bs(a,x): #a->array, x->variable whose position is searched and returned, -1 if not in the array

    l=0
    u=len(a)
    m=int(u/2)

    while(l!=u):
        if x<a[m]:
            u=m-1
        if x>a[m]:
            l=m+1
        m=int((l+u)/2)
        if x==a[m]:
            return m+1
        
    return -1



a=input('Enter you list\n')
b=list(a.split())
a=[int(i) for i in b]

y=input('Enter your list of numbers\n')
z=list(y.split())
y=[int(i) for i in z]


for i in y:
    print(bs(a,i),end=' ')
    
