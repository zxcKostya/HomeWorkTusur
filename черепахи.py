
v1=int(input())
v2=int(input())
g=int(input())
speed=v2-v1
t=g/speed
chas=t//1 #часы
mini=t*60 #минуты
mini2=mini//1
sek=(mini-mini2)*60
sek2=sek//1
if v1>=v2:
    print("nil")
else:
    print(t)
    print(chas,mini2,sek2)
