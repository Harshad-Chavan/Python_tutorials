import random
# a = random.sample(range(10,100),5)
a = [8,7,2,2,4,5,1]
print(a)
l = len(a)
for i in range(0,l-1):
    for j in range(i+1,l):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
            
print(a)