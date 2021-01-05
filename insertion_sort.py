import random
a = random.sample(range(10,100),5)
# a = [8,9,7]
print(a)
l = len(a)
for index in range(1,l):
    current_value = a[index]
    current_postion = index
    while current_postion > 0 and current_value < a[current_postion-1]:
            a[current_postion] = a[current_postion-1]
            current_postion -= 1
    a[current_postion] = current_value

print(a)