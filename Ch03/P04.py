x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 #0.5대신 (1/2)
print("두점 사이의 거리:", distance)
