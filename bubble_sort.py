import random
a = random.sample(range(10,10000),1000)
l = len(a)
swap_count = False
loop_count = 0
for j in range(0,l):
    for i in range(0,l-1-j):
        loop_count += 1
        if a[i] > a[i+1]:
            a[i] , a[i+1] = a[i+1] , a[i]
            swap_count = True
    if not swap_count:
        break
print(a)
print(swap_count)
print(loop_count)

#optimized bubble sort
#check if there are no swaps in one pass...if there are no swaps it means its already sorted