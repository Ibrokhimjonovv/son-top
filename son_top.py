from random import *
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = '*'
a = choice(lis)
b = choice(lis)
print(lis)
for i in range(7):
    son = int(input("Son>>: "))
    if a==son or b==son:
        del lis[son-1]
        lis.insert(son-1, x)    
        print(f"{lis} Afsus pishtiz\nBu {a} va {b} raqamlarda bomba bor edi")
        break
else:
    print(f"Siz g'olibsiz\nBombalar {a} va {b} sonlarda edi")
