a = int(input())
places = list(map(int, input().split()))
b = [0] * (a + 1) 
for k in range(a):
    place = places[k]  
    b[place] = k + 1   
for k in range(1, a + 1):
    print(b[k], end=" ")