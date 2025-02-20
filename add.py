import sys
value = sys.argv[1:]

a = int(value[0]) - 1
b = int(value[1])
c = a + b 
num = a
while num < c:
    num = num +1 
    for x in range(1,10):
        print(f"{num} X {x} = {num*x}")

