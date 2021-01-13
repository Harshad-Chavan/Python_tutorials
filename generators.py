# def fibo_gen(n):
#     a = 0
#     b = 1
#     for _ in range(1,n):
#         sumx = a + b
#         yield b
#         a = b
#         b = sumx

# print(list(fibo_gen(10)))
from random import randint
def gen_squares(low,high):
    for _ in range(low,high):
        
        yield randint(low,high)

print(list(gen_squares(1,10)))