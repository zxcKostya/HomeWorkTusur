a=input()
kilo=int(input())
def kb(kilo):
    print(kilo*1024)

def b(kilo):
    print(kilo/1024)

if a=="байт":
    b(kilo)
else:
    kb(kilo)
    