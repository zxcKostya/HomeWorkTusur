x=int(input())
a=x//1000 #1
b=x%1000//100 #2
c=x%1000%100//10 #3
d=x%1000%100%10//1 #4
a1=a**2
b1=b**2
c1=c**2
d1=d**2
a2=str(a1)
b2=str(b1)
c2=str(c1)
d2=str(d1)
g=a2+b2+c2+d2
print(g)

