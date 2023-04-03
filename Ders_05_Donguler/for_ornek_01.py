for i in range(16):
#    a = 16 - i
#    yazdirma = "{0:3} {1:" + str(a) + "} {2:" + str(i) + "}"
#    print(yazdirma.format(i,"."*a,10**i))
    print("{0:3} {1:16}".format(i, 10 ** i))


for a in range(20):
    print("{0:5}  {1:20}".format(a, 10 ** a))


