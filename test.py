line = [0,1,2,3,4,5,6,7,8]

for i in range(len(line)):
  box = i // 3
  for j in range(box*3, box*3+3):
    print(j)