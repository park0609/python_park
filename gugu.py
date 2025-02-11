import sys
value = sys.argv[1:]

b = list(value[0])
c = set(b)
d = list(c)
if d[0] == '단':
    num = int(d[1]) - 1
    e = num + int(value[1])
    while num < int(e):
         num = num +1 
         print(f"{num}단")
         for x in range(1,10):
             print(f"{num} X {x} = {num*x}")

