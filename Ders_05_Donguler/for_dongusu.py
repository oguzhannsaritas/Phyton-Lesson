for n in range(1,6):
    print(n)
print("\n")
for a in range(1,11):
    print(a, end=" ")
print("\a")




for c in range(21):
    print(c, end=" ")
    if c == 10:
        c = 5
        print("({})".format(c), end=" ")
print()