from array import *

arr = array('i', [1,2,3,4,5])
print(arr.buffer_info())
print(arr[2])
for i in arr:
    print(i)

for pnt in range(1,3):
    print(pnt, arr[pnt])

arr.reverse()
print(arr)

arr.append(19)
print(arr)

arr.remove(3)
print(arr)

# let's assume there was two number 2

arr = array('i',[1,2,2,3,4,5])
arr.remove(2)
print(arr)

# let's say i want to print the index

print(arr[3])
print(arr.index(4))

arr = array('i',[])
x = int(input('Enter the size of the array declared'))
print('enter %d elements' %x)
for i in range(x):
    n= int(input())
    arr.append(n)
print(arr)

# remove duplicate for the array

#arr=array('i'[1,2,3,3,4,5,6,6])
i = 0
while i<x-1:
    j=i+1
    while j<x:
        if arr[i] == arr[j]:
            del arr[j]
            x=x-1
        j+1
    i += 1
print(arr)