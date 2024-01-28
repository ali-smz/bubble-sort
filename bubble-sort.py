import time
#definiting variables
lst=[]
lst_odd=[]
lst_even=[]
n = len(lst)
z=len(lst_even)
h=len(lst_odd)
x=int(input('number of elements : '))

##list creator
for z in range(x):
    m=int(input("number : "))
    lst.append(m)

###list seprator
for m in lst:
    if m %2 == 0:
        lst_even.append(m)
    else:
        lst_odd.append(m)


#### function for sorting    
def sort(lst):
    for i in range(n):
        for j in range(n-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1] , lst[j]
        else:
            continue

def sort_odd(lst_odd):
    for i in range(h):
        for j in range(h-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1] , lst[j]
        else:
            continue

def sort_even(lst_even):
    for i in range(z):
        for j in range(z-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1] , lst[j]
        else:
            continue


##### printing final reasults
print('unsorted list is : ', lst )
lst.sort()
lst_even.sort()
lst_odd.sort()
print("sorted list is : " ,lst)
print('even list is : ',lst_even)
print('odd list is : ',lst_odd)

# time.sleep(60)
 