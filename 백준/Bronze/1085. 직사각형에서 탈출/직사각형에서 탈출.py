x,y,w,h = map(int, input().split())

disX = w - x
disY = h - y

minDis = min(x, y, disX, disY)

print(minDis)