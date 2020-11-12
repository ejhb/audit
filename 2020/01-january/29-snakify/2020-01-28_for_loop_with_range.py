# series -1

a = int(input("enter nb_a"))
b = int(input("enter nb_b"))

for i in range(a,b + 1):
    print(i)

# series -2

a = int(input())
b = int(input())


if a < b :
    for i in (range(a,b +1)):
        print(i)
elif a >= b :
    for i in reversed((range(b,a + 1))):
        print(i)
else :
    print("tozz")

# Sum of ten numbers

x = []
for i in range(10):
    a = x.append(int(input()))

print(sum(x))

